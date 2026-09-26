import json

from tools.inventory import get_inventory
from tools.products import get_product_requirements

# Load customer order
with open("data/order.json", "r") as file:
    order = json.load(file)


# Load inventory using our tool
inventory = get_inventory()

product_name = order["product"]
quantity = order["quantity"]

requirements = get_product_requirements(product_name)

print("\nREQUIRED MATERIALS:")

for material, amount_per_product in requirements.items():
    total_required = amount_per_product * quantity
    print(material, total_required)

print("\nPURCHASE LIST:")

for material, amount_per_product in requirements.items():
    total_required = amount_per_product * quantity
    in_stock = inventory.get(material, 0)

    missing = total_required - in_stock

    if missing > 0:
        print(material, missing)

print("ORDER:")
print(order)

print("\nINVENTORY:")
print(inventory)
