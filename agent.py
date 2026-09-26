import ollama

from tools.inventory import get_inventory
from tools.products import get_product_requirements
from tools.purchasing import calculate_purchase_list

def inventory_tool():
    """Get the current factory inventory."""
    return get_inventory()

def product_requirements_tool(product_name: str):
    """Get the materials required to manufacture one unit of a product."""
    return get_product_requirements(product_name)

def purchase_list_tool(product_name: str, quantity: int):
    """Calculate the exact purchase list for a product order."""

    requirements = get_product_requirements(product_name)
    inventory = get_inventory()

    purchase_list = calculate_purchase_list(
        requirements,
        inventory,
        quantity
    )

    return {
        "product": product_name,
        "quantity": quantity,
        "purchase_list": purchase_list
    }
    
messages = [
    {
        "role": "user",
        "content": "I need to manufacture 2 kitchen_cabinet units. Check the product requirements and current inventory, then tell me what materials I need to purchase. Use the available tools."
    }
]

while True:

    response = ollama.chat(
        model="qwen3:1.7b",
        messages=messages,
        tools=[
            purchase_list_tool
        ]
    )

    messages.append(response.message)

    if response.message.tool_calls:

        for call in response.message.tool_calls:
            print("\nTOOL SELECTED:", call.function.name)
            print("ARGUMENTS:", call.function.arguments)

            if call.function.name == "inventory_tool":
                result = inventory_tool()

            elif call.function.name == "product_requirements_tool":
                product_name = call.function.arguments["product_name"]
                result = product_requirements_tool(product_name)
            elif call.function.name == "purchase_list_tool":
                product_name = call.function.arguments["product_name"]
                quantity = call.function.arguments["quantity"]

                result = purchase_list_tool(product_name, quantity)

            print("TOOL RESULT:")
            print(result)

            messages.append(
                {
                    "role": "tool",
                    "tool_name": call.function.name,
                    "content": str(result)
                }
            )

    else:
        print("\nFINAL ANSWER:")
        print(response.message.content)
        break
