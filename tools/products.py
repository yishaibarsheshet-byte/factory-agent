import json


def get_product_requirements(product_name):
    with open("data/products.json", "r") as file:
        products = json.load(file)

    return products[product_name]
