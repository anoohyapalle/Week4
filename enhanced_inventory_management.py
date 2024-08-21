
import threading
import time
import json

class Inventory:
    def __init__(self):
        self.items = {}
        self.lock = threading.Lock()

    def add_item(self, item_name, quantity):
        with self.lock:
            if item_name in self.items:
                self.items[item_name] += quantity
            else:
                self.items[item_name] = quantity
            print(f"Added {quantity} of {item_name}. Total: {self.items[item_name]}")

    def remove_item(self, item_name, quantity):
        with self.lock:
            if item_name in self.items and self.items[item_name] >= quantity:
                self.items[item_name] -= quantity
                print(f"Removed {quantity} of {item_name}. Total: {self.items[item_name]}")
            else:
                print(f"Cannot remove {quantity} of {item_name}. Not enough in stock.")

    def check_stock(self, item_name):
        with self.lock:
            return self.items.get(item_name, 0)

    def save_to_file(self, filename):
        try:
            with open(filename, 'w') as file:
                json.dump(self.items, file)
            print(f"Inventory saved to {filename}")
        except IOError as e:
            print(f"Error saving inventory to file: {e}")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                self.items = json.load(file)
            print(f"Inventory loaded from {filename}")
        except IOError as e:
            print(f"Error loading inventory from file: {e}")
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON file: {e}")

    def check_stock_levels(self):
        with self.lock:
            for item_name, quantity in self.items.items():
                if quantity < 5:  # Threshold for low stock
                    print(f"Restock Alert: {item_name} is low in stock! ({quantity} left)")

    def start_stock_monitoring(self, interval=10):
        def monitor():
            while True:
                self.check_stock_levels()
                time.sleep(interval)
        
        monitoring_thread = threading.Thread(target=monitor, daemon=True)
        monitoring_thread.start()

inventory = Inventory()

inventory.add_item("Apples", 10)
inventory.add_item("Oranges", 3)
inventory.add_item("Bananas", 15)

inventory.remove_item("Apples", 2)
inventory.remove_item("Oranges", 1)

inventory.save_to_file("inventory.json")

inventory.load_from_file("inventory.json")
print("Current inventory:", inventory.items)

inventory.start_stock_monitoring(interval=5)

time.sleep(20) 
