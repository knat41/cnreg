"""
main_loader.py
Robust dataset loader using only fastparquet (no pyarrow fallback).
"""

import argparse
import sys
from pathlib import Path
import logging
import pandas as pd

from data_loader import DataLoader
from cn_var import getData2Frame, getCNPDF

logger = logging.getLogger(__name__)
if not logger.handlers:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def safe_to_parquet(df: pd.DataFrame, path: Path):
    """
    Save DataFrame using ONLY fastparquet engine.
    """
    try:
        df.to_parquet(str(path), engine="fastparquet", index=False)
        logger.info(f"Saved parquet to {path} using fastparquet")
    except Exception as e:
        logger.error(f"Failed to save parquet (fastparquet): {e}")
        raise


def safe_read_parquet(path: Path) -> pd.DataFrame:
    """
    Read DataFrame using ONLY fastparquet engine.
    """
    try:
        return pd.read_parquet(str(path), engine="fastparquet")
    except Exception as e:
        logger.error(f"Failed to read parquet (fastparquet): {e}")
        raise


def main(argv=None):
    parser = argparse.ArgumentParser(description="Create or load dataset.")
    parser.add_argument("--data-dir", "-d", default="data")
    parser.add_argument("--create", "-c", action="store_true")
    parser.add_argument("--parquet-all", default="all68_m3.parquet")
    parser.add_argument("--parquet-m3", default="68_m3.parquet")
    parser.add_argument("--parquet-gpa", default="gpa68_m3.parquet")
    parser.add_argument("--threads", action="store_true")
    parser.add_argument("--progress", action="store_true")
    parser.add_argument("--recursive", action="store_true")
    args = parser.parse_args(argv)

    data_dir = Path(args.data_dir)
    if not data_dir.exists():
        logger.error(f"Data directory not found: {data_dir}")
        sys.exit(1)

    if args.create:
        loader = DataLoader(
            directory=str(data_dir),
            recursive=args.recursive,
            header_candidates=[0, 1],
            encoding="utf-8",
            on_error="skip",
            use_threads=args.threads,
            max_workers=8 if args.threads else 1,
            show_progress=args.progress,
        )

        all_student, failed = loader.load_all()
        logger.info(f"Combined rows: {len(all_student)}")

        if failed:
            logger.warning(f"{len(failed)} files failed to read:")
            for f in failed:
                logger.warning(f" - {f['path']}: {f['error']}")

        try:
            m3_student = getData2Frame(all_student)
        except Exception as e:
            logger.error(f"getData2Frame failed: {e}")
            m3_student = all_student

        # Save parquet (fastparquet only)
        safe_to_parquet(all_student, Path(args.parquet_all))
        safe_to_parquet(m3_student, Path(args.parquet_m3))

    else:
        # Load old parquet
        try:
            all_student = safe_read_parquet(Path(args.parquet_all))
            m3_student = safe_read_parquet(Path(args.parquet_m3))
        except Exception as e:
            logger.error(f"Error loading parquet: {e}")
            sys.exit(1)

    # load gpa if available
    p_gpa = Path(args.parquet_gpa)
    if p_gpa.exists():
        try:
            gpa_m3 = safe_read_parquet(p_gpa)
        except Exception:
            gpa_m3 = pd.DataFrame()
    else:
        gpa_m3 = pd.DataFrame()

    m3 = [m3_student, gpa_m3]

    # ▼ ตัวอย่าง reqlist ของคุณ ▼
    reqlist = [
        44132, 44149, 44150, 44151, 44188, 44220, 44220, 44228, 44230, 44233,
        44239, 44260, 44263, 44274, 44364, 44380, 44404, 44416, 44435, 44439,
        44464, 44465, 44477, 44485, 44504, 44555, 44556, 44564, 44566, 44572,
        44574, 44626, 44642, 44648, 44649, 44658, 44666, 44680, 44686, 44688,
        44712, 44751, 44495, 44176, 44603, 44736, 44558, 44431, 44311, 44124,
        44394, 44224, 44623, 44168, 44193, 44473, 44217, 44391, 44429, 44125,
        44679, 44290, 44138, 44185, 44432, 44513, 44376, 44457, 44373, 44171
    ]

    for idnumber in reqlist:
        try:
            getCNPDF(m3, idnumber)
        except Exception as e:
            logger.error(f"PDF failed for {idnumber}: {e}")

    logger.info("DONE.")


if __name__ == "__main__":
    main()
