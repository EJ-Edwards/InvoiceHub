from generator import generator
from pdf import pdf
from calculator import calculator


CONTACT_EMAIL = "ee1912136@gmail.com"
GITHUB_URL = "https://github.com/EJ-Edwards/InvoiceHub"


def show_terms():
    print("\n===== TERMS OF SERVICE =====\n")
    print(
        "InvoiceHub is provided \"as is\" with no warranty of any kind.\n"
        "You are responsible for verifying all invoice data before use.\n"
        "The creators are not liable for financial loss, incorrect billing,\n"
        "or tax-related issues.\n\n"
        "InvoiceHub does not provide legal, tax, or accounting advice.\n"
        "By continuing to use this software, you agree to these terms.\n"
    )
    print("Need help or have questions?")
    print(f"Contact: {CONTACT_EMAIL}")
    print(f"GitHub: {GITHUB_URL}")
    print("\n============================\n")


def accept_terms():
    show_terms()

    while True:
        choice = input("Do you accept the Terms of Service? (y/n): ").lower()

        if choice == "y":
            return True
        elif choice == "n":
            print("\nYou must accept the terms to use InvoiceHub.")
            return False
        else:
            print("Please enter 'y' or 'n'.")


def menu():
    if not accept_terms():
        return

    while True:
        print("\nInvoiceHub CLI")
        print("1. Generate Invoice")
        print("2. View PDF")
        print("3. Calculate Total")
        print("4. Contact / Help")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            generator()
        elif choice == "2":
            pdf()
        elif choice == "3":
            calculator()
        elif choice == "4":
            print("\n===== CONTACT =====")
            print(f"Email: {CONTACT_EMAIL}")
            print(f"GitHub: {GITHUB_URL}")
        elif choice == "5":
            print("Goodbye 👋")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    menu()
