products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}


def get_product(code):

    return products[code]


def get_property(code, property):

    return products[code][property]


def main():

    inp = ""
    orders = {}
    total = 0

    while inp != "/":
        subtotal = 0
        order = input("Enter your order: {code}, {quantity} ")
        if order != "/":
            code, quantity = order.split(", ")
            product = get_product(code)
        else:
            break

        quantity = int(quantity)
        price = product["price"]
        subtotal = price * quantity

        if code in orders.keys():
            orders[code]["quantity"] += quantity
            orders[code]["subtotal"] += subtotal
        else:
            orders[code] = {
                "quantity" :  quantity,
                "subtotal" : subtotal
            }

        total += subtotal

    orders = dict(sorted(orders.items()))
    output = []
    output.append('==')
    output.append('CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL')

    for code, order in orders.items():
        name = get_property(code, "name")
        quantity = order["quantity"]
        subtotal = order["subtotal"]
        output.append(f'{code}\t\t{name}\t\t{quantity}\t\t\t\t{subtotal}')

    output.append("")
    output.append(f'Total:\t\t\t\t\t\t\t\t\t\t{total}')
    output.append('==')
    output = "\n".join(output)

    print(output)

    with open("receipt.txt", "w") as f:
        f.write(output)

main()
