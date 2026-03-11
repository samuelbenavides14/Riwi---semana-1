
#In this entry, we ask the user to enter the name of the article.
article = str(input("Enter the article name: "))

def price_required():
    try:
        price = float(input("Enter the price of the item: "))

        if price <= 0:
            print("try again")
            return price_required()
    except ValueError:
        print("try again")
        return price_required()
    return price


def required_quantity():
    try:
        amount = int(input("Enter the amount: "))
        if amount <= 0:
            print("try again")
            return required_quantity()
    except ValueError:
        print("try again")
        return required_quantity()
    return amount



price = price_required()
amount = required_quantity()

#In this step, the algorithm prints on the screen the name, price, and quantity of the entered item.
print(f"Article title: {article}")
print(f"price of the item: {price}")
print(f"existence of the article: {amount}" )