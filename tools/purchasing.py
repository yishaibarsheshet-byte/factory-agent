def calculate_purchase_list(requirements, inventory, quantity):
    purchase_list = {}

    for material, amount_per_product in requirements.items():
        total_required = amount_per_product * quantity
        in_stock = inventory.get(material, 0)

        missing = total_required - in_stock

        if missing > 0:
            purchase_list[material] = missing

    return purchase_list
