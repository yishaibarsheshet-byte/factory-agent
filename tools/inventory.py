import json


def get_inventory():
    with open("data/inventory.json", "r") as file:
        inventory = json.load(file)

    return inventory
