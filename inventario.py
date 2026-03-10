
#In this entry, we ask the user to enter the name of the article.
article = str(input("Enter the article name: "))

def price_required():
    price = float(input("Enter the price of the item: "))
    while price <= 0:
        try:
            if price <= 0:
                print("try again")
                return price_required()
        except ValueError:
            print("try again")
        return price_required()
    return price





def required_quantity():
    amount = int(input("Enter the amount: "))
    while amount <= 0:
        try:
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