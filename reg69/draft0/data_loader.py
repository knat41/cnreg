"""
data_loader.py
Robust cross-platform DataLoader utility for tabular files.

Features:
- Uses pathlib for cross-platform paths (Linux/Mac/Windows)
- Supports .xls/.xlsx/.csv/.htm/.html by trying multiple readers
- Flexible header detection (header_candidates)
- Error handling with failed-files report
- Optional multi-threaded reading for IO-bound workloads
- Optional progress reporting via tqdm (if installed)
- Returns (combined_df, failed_list)
"""

from pathlib import Path
from typing import List, Tuple, Optional, Iterable, Dict, Any
import pandas as pd
import logging
import concurrent.futures
import traceback

# Basic logger (users can configure logging in their app)
logger = logging.getLogger(__name__)
if not logger.handlers:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


class DataLoader:
    def __init__(
        self,
        directory: str,
        patterns: Optional[Iterable[str]] = None,
        recursive: bool = False,
        header_candidates: Optional[List[Optional[int]]] = None,
        encoding: str = "utf-8",
        on_error: str = "skip",  # 'skip' or 'raise'
        use_threads: bool = False,
        max_workers: int = 4,
        show_progress: bool = False,
    ):
        """
        :param directory: path to search files
        :param patterns: glob patterns (default: xls,xlsx,csv,htm,html)
        :param recursive: whether to search recursively
        :param header_candidates: list of header row indexes to try (e.g. [0,1])
                                  use None to try header=None
        :param encoding: default encoding for read_html/read_csv
        :param on_error: 'skip' to continue on read errors, 'raise' to raise Immediately
        :param use_threads: if True, uses ThreadPoolExecutor to read multiple files concurrently
        :param max_workers: number of threads to use when use_threads=True
        :param show_progress: if True and tqdm is installed, show progress bar
        """
        self.dir = Path(directory)
        if patterns is None:
            self.patterns = ["*.xls", "*.xlsx", "*.csv", "*.htm", "*.html"]
        else:
            self.patterns = list(patterns)
        self.recursive = recursive
        self.header_candidates = header_candidates if header_candidates is not None else [0, 1]
        self.encoding = encoding
        assert on_error in ("skip", "raise"), "on_error must be 'skip' or 'raise'"
        self.on_error = on_error
        self.use_threads = use_threads
        self.max_workers = max_workers
        self.show_progress = show_progress

    def find_files(self) -> List[Path]:
        files = []
        for pat in self.patterns:
            if self.recursive:
                files.extend(self.dir.rglob(pat))
            else:
                files.extend(self.dir.glob(pat))
        files = sorted(set(files))
        logger.info(f"DataLoader: found {len(files)} files matching {self.patterns} in {self.dir}")
        return files

    def _try_read_html(self, p: Path) -> Optional[pd.DataFrame]:
        try:
            tables = pd.read_html(p, encoding=self.encoding)
            if tables:
                return tables[0]
        except Exception:
            return None

    def _try_read_excel(self, p: Path, header: Optional[int]) -> Optional[pd.DataFrame]:
        try:
            # pandas can infer engine; user can set engine if needed by environment
            return pd.read_excel(p, header=header)
        except Exception:
            return None

    def _try_read_csv(self, p: Path) -> Optional[pd.DataFrame]:
        try:
            return pd.read_csv(p, encoding=self.encoding)
        except Exception:
            return None

    def read_one(self, p: Path) -> Tuple[Optional[pd.DataFrame], Optional[str]]:
        """
        Attempt to read one file using several strategies.
        Returns (df, None) on success, (None, error_message) on failure.
        """
        suffix = p.suffix.lower()
        # 1) CSV
        if suffix == ".csv":
            df = self._try_read_csv(p)
            if df is not None:
                return df, None
            return None, "read_csv_failed"

        # 2) HTML tables inside file (covers html files and some xls that are HTML-wrapped)
        df = self._try_read_html(p)
        if df is not None:
            return df, None

        # 3) Excel attempts for .xls/.xlsx (try header candidates)
        if suffix in (".xls", ".xlsx"):
            for h in self.header_candidates:
                try:
                    df = self._try_read_excel(p, header=h)
                except Exception:
                    df = None
                if df is not None:
                    return df, None
            # final attempt header=None
            df = self._try_read_excel(p, header=None)
            if df is not None:
                return df, None
            return None, "read_excel_failed"

        # 4) For other suffixes, try generic excel reader as last resort
        try:
            df = pd.read_excel(p)
            if df is not None:
                return df, None
        except Exception:
            pass

        return None, "no_reader_succeeded"

    def _process_files_sequential(self, files: List[Path]) -> Tuple[List[pd.DataFrame], List[Dict[str, Any]]]:
        dflist: List[pd.DataFrame] = []
        failed: List[Dict[str, Any]] = []
        use_tqdm = False
        if self.show_progress:
            try:
                from tqdm import tqdm  # type: ignore
                use_tqdm = True
            except Exception:
                use_tqdm = False

        iterator = files
        if use_tqdm:
            from tqdm import tqdm  # type: ignore
            iterator = tqdm(files, desc="Reading files", unit="file")

        for p in iterator:
            try:
                df, err = self.read_one(p)
            except Exception as e:
                df, err = None, f"exception: {e}\n{traceback.format_exc()}"
            if df is None:
                failed.append({"path": str(p), "error": err})
                logger.warning(f"Failed reading {p}: {err}")
                if self.on_error == "raise":
                    raise RuntimeError(f"Failed reading {p}: {err}")
            else:
                dflist.append(df)
                logger.info(f"Read OK: {p} rows={len(df)}")
        return dflist, failed

    def _process_files_threaded(self, files: List[Path]) -> Tuple[List[pd.DataFrame], List[Dict[str, Any]]]:
        dflist: List[pd.DataFrame] = []
        failed: List[Dict[str, Any]] = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as ex:
            futures = {ex.submit(self.read_one, p): p for p in files}
            if self.show_progress:
                try:
                    from tqdm import tqdm  # type: ignore
                    futures_iter = concurrent.futures.as_completed(futures)
                    for fut in tqdm(futures_iter, total=len(futures), desc="Reading files", unit="file"):
                        p = futures[fut]
                        try:
                            df, err = fut.result()
                        except Exception as e:
                            df, err = None, f"exception: {e}\n{traceback.format_exc()}"
                        if df is None:
                            failed.append({"path": str(p), "error": err})
                            logger.warning(f"Failed reading {p}: {err}")
                            if self.on_error == "raise":
                                raise RuntimeError(f"Failed reading {p}: {err}")
                        else:
                            dflist.append(df)
                            logger.info(f"Read OK: {p} rows={len(df)}")
                except Exception:
                    # fallback: collect without tqdm
                    for fut in concurrent.futures.as_completed(futures):
                        p = futures[fut]
                        try:
                            df, err = fut.result()
                        except Exception as e:
                            df, err = None, f"exception: {e}\n{traceback.format_exc()}"
                        if df is None:
                            failed.append({"path": str(p), "error": err})
                            logger.warning(f"Failed reading {p}: {err}")
                            if self.on_error == "raise":
                                raise RuntimeError(f"Failed reading {p}: {err}")
                        else:
                            dflist.append(df)
                            logger.info(f"Read OK: {p} rows={len(df)}")
            else:
                # no progress bar
                for fut in concurrent.futures.as_completed(futures):
                    p = futures[fut]
                    try:
                        df, err = fut.result()
                    except Exception as e:
                        df, err = None, f"exception: {e}\n{traceback.format_exc()}"
                    if df is None:
                        failed.append({"path": str(p), "error": err})
                        logger.warning(f"Failed reading {p}: {err}")
                        if self.on_error == "raise":
                            raise RuntimeError(f"Failed reading {p}: {err}")
                    else:
                        dflist.append(df)
                        logger.info(f"Read OK: {p} rows={len(df)}")
        return dflist, failed

    def load_all(self, concat_ignore_index: bool = True) -> Tuple[pd.DataFrame, List[Dict[str, Any]]]:
        """
        Load all files discovered. Returns (combined_dataframe, failed_files_list).
        failed_files_list entries: {"path": str, "error": str}
        """
        files = self.find_files()
        if not files:
            logger.info("No files to load.")
            return pd.DataFrame(), []

        if self.use_threads:
            dflist, failed = self._process_files_threaded(files)
        else:
            dflist, failed = self._process_files_sequential(files)

        if dflist:
            try:
                combined = pd.concat(dflist, ignore_index=concat_ignore_index)
            except Exception as e:
                logger.error(f"Failed to concat dataframes: {e}")
                # return what we have concatenated incrementally as fallback
                combined = pd.DataFrame()
                for df in dflist:
                    combined = pd.concat([combined, df], ignore_index=True)
        else:
            combined = pd.DataFrame()

        return combined, failed
