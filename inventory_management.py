product_names = ["Apples", "Bananas", "Oranges"]

def add_product(name):
    if name not in product_names:
        product_names.append(name)
        print(f"Product '{name}' added.")
    else:
        print(f"Product '{name}' already exists.")

def remove_product(name):
    if name in product_names:
        product_names.remove(name)
        print(f"Product '{name}' removed.")
    else:
        print(f"Product '{name}' not found.")

def update_product(old_name, new_name):
    if old_name in product_names:
        index = product_names.index(old_name)
        product_names[index] = new_name
        print(f"Product '{old_name}' updated to '{new_name}'.")
    else:
        print(f"Product '{old_name}' not found.")

add_product("Grapes")
remove_product("Bananas")
update_product("Oranges", "Mandarins")
print("Product names:", product_names)

product_details = {
    "Apples": {"quantity": 50, "price": 0.5},
    "Bananas": {"quantity": 30, "price": 0.3},
}

def add_product_detail(name, quantity, price):
    if name not in product_details:
        product_details[name] = {"quantity": quantity, "price": price}
        print(f"Product '{name}' added with quantity {quantity} and price ${price:.2f}.")
    else:
        print(f"Product '{name}' already exists.")

def update_product_detail(name, quantity=None, price=None):
    if name in product_details:
        if quantity is not None:
            product_details[name]["quantity"] = quantity
        if price is not None:
            product_details[name]["price"] = price
        print(f"Product '{name}' updated.")
    else:
        print(f"Product '{name}' not found.")

def delete_product_detail(name):
    if name in product_details:
        del product_details[name]
        print(f"Product '{name}' deleted.")
    else:
        print(f"Product '{name}' not found.")

add_product_detail("Oranges", 40, 0.4)
update_product_detail("Apples", price=0.55)
delete_product_detail("Bananas")
print("Product details:", product_details)

immutable_product_data = (
    ("SKU001", "Apples", 0.5),
    ("SKU002", "Bananas", 0.3),
    ("SKU003", "Oranges", 0.4),
)

def display_product_catalog():
    for sku, name, price in immutable_product_data:
        print(f"SKU: {sku}, Product: {name}, Price: ${price:.2f}")

print("Product Catalog:")
display_product_catalog()

product_categories = {"Fruits", "Vegetables", "Dairy"}

def add_category(category):
    if category not in product_categories:
        product_categories.add(category)
        print(f"Category '{category}' added.")
    else:
        print(f"Category '{category}' already exists.")

def remove_category(category):
    if category in product_categories:
        product_categories.remove(category)
        print(f"Category '{category}' removed.")
    else:
        print(f"Category '{category}' not found.")

add_category("Beverages")
remove_category("Dairy")
print("Product categories:", product_categories)

def generate_price_report():
    sorted_products = sorted(product_details.items(), key=lambda x: x[1]["price"])
    print("Products sorted by price:")
    for name, details in sorted_products:
        print(f"Product: {name}, Price: ${details['price']:.2f}")

def find_products_in_price_range(min_price, max_price):
    products_in_range = {name for name, details in product_details.items() if min_price <= details["price"] <= max_price}
    print(f"Products in price range ${min_price:.2f} - ${max_price:.2f}: {products_in_range}")

generate_price_report()
find_products_in_price_range(0.4, 0.6)
