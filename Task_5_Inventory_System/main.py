
from models import Book, Magazine, DigitalMedia
from inventory import InventoryManager


def read_price():
    while True:
        try:
            price = float(input("Enter price (Rs.): "))

            if price <= 0:
                print("Price must be greater than zero.")
                continue

            return price

        except ValueError:
            print("Please enter a valid numeric price.")


def add_book(manager):
    print("\n--- ADD BOOK ---")

    item_id = input("Enter Book ID: ").strip()
    title = input("Enter Book Title: ").strip()
    author = input("Enter Author Name: ").strip()
    price = read_price()

    book = Book(item_id, title, author, price)
    manager.add_item(book)

    print("\nBook added successfully.")


def add_magazine(manager):
    print("\n--- ADD MAGAZINE ---")

    item_id = input("Enter Magazine ID: ").strip()
    title = input("Enter Magazine Title: ").strip()
    issue = input("Enter Issue Number: ").strip()
    price = read_price()

    magazine = Magazine(item_id, title, issue, price)
    manager.add_item(magazine)

    print("\nMagazine added successfully.")


def add_digital_media(manager):
    print("\n--- ADD DIGITAL MEDIA ---")

    item_id = input("Enter Digital Media ID: ").strip()
    title = input("Enter Title: ").strip()
    file_format = input("Enter File Format: ").strip()

    duration = int(input("Enter Duration (minutes): "))
    price = read_price()

    media = DigitalMedia(
        item_id,
        title,
        file_format,
        duration,
        price
    )

    manager.add_item(media)

    print("\nDigital media added successfully.")


def search_item(manager):
    item_id = input("\nEnter Item ID to search: ").strip()
    item = manager.search_item(item_id)

    if item:
        print("\nItem Found:")
        print(item.display_metadata())
        print("Status:", "Borrowed" if item.is_borrowed else "Available")
    else:
        print("\nItem not found.")


def checkout_item(manager):
    item_id = input("\nEnter Item ID to checkout: ").strip()

    item = manager.checkout_item(item_id)

    print(f"\nSuccessfully checked out: {item.title}")


def return_item(manager):
    item_id = input("\nEnter Item ID to return: ").strip()

    fee = manager.return_item(item_id)

    print("\nItem returned successfully.")
    print(f"Borrowing Fee: Rs. {fee:.2f}")


def show_menu():
    print("\n")
    print("=" * 50)
    print("       SMART INVENTORY & ASSET SYSTEM")
    print("=" * 50)
    print("1. Add Book")
    print("2. Add Magazine")
    print("3. Add Digital Media")
    print("4. Display All Inventory")
    print("5. Search Item")
    print("6. Checkout Item")
    print("7. Return Item")
    print("8. Generate Audit Report")
    print("9. Show Total Inventory Count")
    print("0. Exit")
    print("=" * 50)


def main():
    manager = InventoryManager()

    print("\nWelcome to the Smart Inventory & Asset System!")

    while True:
        show_menu()

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                add_book(manager)

            elif choice == "2":
                add_magazine(manager)

            elif choice == "3":
                add_digital_media(manager)

            elif choice == "4":
                manager.display_inventory()

            elif choice == "5":
                search_item(manager)

            elif choice == "6":
                checkout_item(manager)

            elif choice == "7":
                return_item(manager)

            elif choice == "8":
                manager.generate_audit_report()

            elif choice == "9":
                print(f"\nTotal Items: {len(manager)}")
                print(manager)

            elif choice == "0":
                print("\nThank you for using the Inventory System.")
                print("Goodbye!")
                break

            else:
                print("\nInvalid choice. Please select a valid option.")

        except (ValueError, TypeError) as error:
            print(f"\nError: {error}")

        except Exception as error:
            print(f"\nUnexpected error: {error}")


if __name__ == "__main__":
    main()
