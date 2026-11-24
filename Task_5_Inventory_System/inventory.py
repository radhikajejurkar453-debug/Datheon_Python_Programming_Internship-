
from datetime import datetime
from models import Item


class InventoryManager:

    def __init__(self):
        self._items = {}
        self._audit_log = []

    def _record_audit(self, action, item_id, details):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self._audit_log.append({
            "timestamp": timestamp,
            "action": action,
            "item_id": item_id,
            "details": details
        })

    def add_item(self, item):
        if not isinstance(item, Item):
            raise TypeError("Only valid Item objects can be added.")

        if item.item_id in self._items:
            raise ValueError("An item with this ID already exists.")

        self._items[item.item_id] = item

        self._record_audit(
            "ADD",
            item.item_id,
            f"Added {item.__class__.__name__}: {item.title}"
        )

    def search_item(self, item_id):
        return self._items.get(str(item_id).strip())

    def display_inventory(self):
        if not self._items:
            print("\nInventory is empty.")
            return

        print("\n" + "=" * 90)
        print("                         INVENTORY LIST")
        print("=" * 90)

        for item in self._items.values():
            print(item.display_metadata())
            print(
                "Status:",
                "Borrowed" if item.is_borrowed else "Available"
            )
            print("-" * 90)

        print(f"Total inventory items: {len(self)}")

    def checkout_item(self, item_id):
        item = self.search_item(item_id)

        if item is None:
            raise ValueError("Item ID not found.")

        item.checkout()

        self._record_audit(
            "CHECKOUT",
            item.item_id,
            f"Checked out {item.title}"
        )

        return item

    def return_item(self, item_id):
        item = self.search_item(item_id)

        if item is None:
            raise ValueError("Item ID not found.")

        fee = item.return_item()

        self._record_audit(
            "RETURN",
            item.item_id,
            f"Returned {item.title}; Fee: Rs. {fee:.2f}"
        )

        return fee

    def generate_audit_report(self):
        print("\n" + "=" * 105)
        print("                              INVENTORY AUDIT REPORT")
        print("=" * 105)

        if not self._audit_log:
            print("No inventory activities recorded.")
            return

        print(
            f"{'Timestamp':<22}"
            f"{'Action':<12}"
            f"{'Item ID':<12}"
            f"Details"
        )

        print("-" * 105)

        for record in self._audit_log:
            print(
                f"{record['timestamp']:<22}"
                f"{record['action']:<12}"
                f"{record['item_id']:<12}"
                f"{record['details']}"
            )

        print("=" * 105)

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return f"InventoryManager with {len(self)} items"

    def __repr__(self):
        return f"InventoryManager(total_items={len(self)})"
