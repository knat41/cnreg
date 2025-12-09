from cn_var import *

m3 = []

def main():
    while True:
        print("\nMenu")
        print("1. Create datafile")
        print("2. Load datafile")
        print("3. Get certificate")
        print("   3.1 CN (getCN, getCNPDF)")
        print("   3.2 CRU (getCRU, getCRUPDF)")
        print("4. Quit")
        
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            create_datafile()
        elif choice == '2':
            m3 = load_datafile()
            print(*m3)
        elif choice == '3':
            get_certificate()
        elif choice == '3.1':
            getCN()
        elif choice == '3.2':
            getCRU()
        elif choice == '4':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

def get_certificate():
    print("\nSelect Certificate Type:")
    print("3.1 CN getCN")    
    print("3.2 CRU (getCRU, getCRUPDF)")
    print("3.3 CN getCNPDF")
    print("3.4 CRU getCRUPDF")
    sub_choice = input("Enter your choice: ").strip()
    
    if sub_choice == '3.1':
        getCN()
    elif sub_choice == '3.2':
        getCRU()
    elif sub_choice == '3.3':
        getCNPDF()
    elif sub_choice == '3.4':
        getCRUPDF()
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
