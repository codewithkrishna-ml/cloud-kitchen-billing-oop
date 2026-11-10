#PROJECT-Cloud Kitchen / Restaurant Billing System
class MenuItem:
    def __init__(self, item_id, name, price, category):
        self.item_id = int(item_id)
        self.name = name
        self.price = float(price)
        self.category = category

    def get_item_details(self):
        print(f"ID: {self.item_id} | Name: {self.name} | Price: {self.price} | Category: {self.category}")


class Order:
    def __init__(self, order_id, customer_name):
        self.order_id = int(order_id)
        self.customer_name = customer_name
        self.ordered_items = {}
        self.status = "Received"
        self.total_amount = 0.0

    def add_item(self, item_obj, quantity):
        qty = int(quantity)
        if item_obj in self.ordered_items:
            self.ordered_items[item_obj] += qty
        else:
            self.ordered_items[item_obj] = qty
        self.total_amount += item_obj.price * qty


class Kitchen:
    def __init__(self):
        self.pending_orders = []

    def send_to_kitchen(self, order_obj):
        order_obj.status = "Cooking"
        self.pending_orders.append(order_obj)
        print(f"Order ID {order_obj.order_id} sent to kitchen for cooking.")

    def complete_cooking(self, order_id):
        target_order = None
        for order in self.pending_orders:
            if order.order_id == int(order_id):
                target_order = order
                break

        if target_order:
            self.pending_orders.remove(target_order)
            target_order.status = "Ready for Pickup/Delivery"
            print(f"Order ID {order_id} is now cooked and ready!")
            return True
        else:
            print("Order ID not found in the kitchen.")
            return False


class BillingManager:
    def __init__(self):
        self.menu = {}
        self.orders_db = {}
        self.kitchen_dept = Kitchen()
        self.total_revenue = 0.0

    def add_to_menu(self, item_obj):
        if item_obj.item_id in self.menu:
            print("Error: Item ID already exists in the menu!")
            return False
        self.menu[item_obj.item_id] = item_obj
        print(f"Item '{item_obj.name}' added to menu successfully.")
        return True

    def take_new_order(self, order_obj):
        if order_obj.order_id in self.orders_db:
            print("Error: Order ID already exists!")
            return False
        self.orders_db[order_obj.order_id] = order_obj
        print(f"Order initialized for {order_obj.customer_name}.")
        return True

    def add_item_to_order(self, order_id, item_id, quantity):
        oid = int(order_id)
        iid = int(item_id)
        
        if oid not in self.orders_db:
            print("Error: Order ID not found.")
            return False
        if iid not in self.menu:
            print("Error: Item ID not found in the menu.")
            return False

        order = self.orders_db[oid]
        item = self.menu[iid]
        order.add_item(item, quantity)
        print(f"Added {quantity}x '{item.name}' to Order {order_id}.")
        return True

    def generate_bill(self, order_id, discount_percentage=0.0):
        oid = int(order_id)
        if oid not in self.orders_db:
            print("Error: Order ID not found.")
            return

        order = self.orders_db[oid]
        order.status = "Billed"

        amount = order.total_amount
        tax = amount * 0.05
        discount = amount * (float(discount_percentage) / 100.0)
        final_bill = amount + tax - discount
        
        self.total_revenue += final_bill

        print(f"\n--- BILL FOR ORDER ID: {order_id} ---")
        print(f"Customer Name: {order.customer_name}")
        print("-" * 35)
        for item, qty in order.ordered_items.items():
            print(f"{item.name} x {qty}: {item.price * qty}")
        print("-" * 35)
        print(f"Subtotal: {amount}")
        print(f"GST (5%): {tax}")
        print(f"Discount: {discount}")
        print(f"Final Amount to Pay: {final_bill}")
        print("-" * 35)


def main():
    manager = BillingManager()

    while True:
        print("\n" + "="*45)
        print("------- CLOUD KITCHEN / BILLING SYSTEM -------")
        print("="*45)
        print("1. Add Item to Menu")
        print("2. View Menu Card")
        print("3. Create New Customer Order")
        print("4. Add Dish to an Order")
        print("5. Send Order to Kitchen")
        print("6. Complete Kitchen Cooking")
        print("7. Generate Bill & Process Payment")
        print("8. View Total Daily Revenue")
        print("9. Exit")

        choice = input("Select an option (1-9): ").strip()

        if choice == "1":
            iid = int(input("Enter Item ID: ").strip())
            name = input("Enter Item Name: ").strip()
            price = float(input("Enter Item Price: ").strip())
            category = input("Enter Category (Veg/Non-Veg/Beverage): ").strip()
            item = MenuItem(iid, name, price, category)
            manager.add_to_menu(item)

        elif choice == "2":
            if not manager.menu:
                print("Menu is empty.")
            else:
                print("\n--- MENU CARD ---")
                for item_id, item_obj in manager.menu.items():
                    item_obj.get_item_details()

        elif choice == "3":
            oid = int(input("Enter Order ID: ").strip())
            cname = input("Enter Customer Name: ").strip()
            order = Order(oid, cname)
            manager.take_new_order(order)

        elif choice == "4":
            oid = int(input("Enter Order ID: ").strip())
            iid = int(input("Enter Item ID: ").strip())
            qty = int(input("Enter Quantity: ").strip())
            manager.add_item_to_order(oid, iid, qty)

        elif choice == "5":
            oid = int(input("Enter Order ID to send to kitchen: ").strip())
            if oid in manager.orders_db:
                manager.kitchen_dept.send_to_kitchen(manager.orders_db[oid])
            else:
                print("Error: Order ID not found.")

        elif choice == "6":
            oid = int(input("Enter Order ID to mark as cooked: ").strip())
            manager.kitchen_dept.complete_cooking(oid)

        elif choice == "7":
            oid = int(input("Enter Order ID to generate bill: ").strip())
            disc = float(input("Enter Discount % (0 if none): ").strip())
            manager.generate_bill(oid, disc)

        elif choice == "8":
            print(f"\nTotal System Revenue Collected: {manager.total_revenue}")

        elif choice == "9":
            print("\nThank you for using the Cloud Kitchen Billing System. Goodbye!\n")
            break
        else:
            print("\nInvalid choice! Please select between 1 and 9.")


if __name__ == "__main__":
    main()
