# shopping_cart.py

#importing date module
import datetime

###REVISITATION
# Refactoring price formatting logic: Display in USD with two decimals
def to_usd(product_price):
    return "${0:,.2f}".format(product_price)
# Refactoring time stamp formatting logic: Ensures that human friendly current date/time is displayed
def human_friendly_timestamp(date_time):
    return date_time.strftime("%m-%d-%Y %I:%M %p")
# Refactoring get product logic: Displays matching product identifier
def find_product(selected_id, products):
    matching_products= [p for p in products if str(p["id"]) == str(selected_id)]
    matching_product= matching_products[0]
    return matching_product
# Refactoring total price calculation:
#def calculate_total_price(matching_product):
    #total_price= total_price + matching_product["price"]



if __name__ == "__main__":
    #inventory list
    products = [
        {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
        {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
        {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
        {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
        {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
        {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
        {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
        {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
        {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
        {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
        {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
        {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
        {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
        {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
        {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
        {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
        {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
        {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
        {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
        {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
    ] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


    #
    #INFO CAPTURE/ INPUT
    #
    total_price= 0
    selected_ids= []

    while True:
        selected_id = input("Please input a product identifier, or 'DONE' if there are no more items: ")
        if selected_id == "DONE":
            break
        else:
            selected_ids.append(selected_id)
    #

    #Checkpoint 1 DONE


    #print("SHOPPING CART ITEMS IDENTIFIERS INCLUDE: " + str(selected_ids))

    # Checkpoint 2 DONE


    #Print Receipt
    print("--------------------------------")

    # A grocery store name of your choice.
    print("SAMS PLENTIFUL PRODUCE")

    # A grocery store phone number and/or website URL and/or address of choice.
    print("--------------------------------")
    print("CONTACT VIA WEB: SAMS-PLENTIFUL-PRODUCE.com")
    print("CONTACT VIA PHONE: (917)-675-0102")

    # The date and time of the beginning of the checkout process, formatted in a human-friendly way.
    print("--------------------------------")
    print("Checkout Time: ", human_friendly_timestamp(datetime.datetime.now()))

    # The name and price of each shopping cart item, price being formatted as US dollars and cents (e.g. $1.50).
    print("--------------------------------")
    print("Shopping Cart Items:")
    for selected_id in selected_ids:
        ####matching_products= [p for p in products if str(p["id"]) == str(selected_id)]
        ####matching_product= matching_products[0]
        matching_product= find_product(selected_id, products)
        #total_price= total_price + matching_product["price"]
        price_usd = to_usd(matching_product["price"])
        print("+ " + matching_product["name"] + " " + price_usd)

    # The total cost of all shopping cart items, formatted as US dollars and cents (e.g. $4.50), calculated as the sum of their prices.
    print("--------------------------------")
    print("SUBTOTAL:", to_usd(total_price))

    # The amount of tax owed, calculated by multiplying the total cost by a District of Columbia sales tax rate of 6%.
    tax= total_price * .06
    print("+ District of Columbia Sales Tax (6%): ", to_usd(tax))

    # The total amount owed, formatted as US dollars and cents (e.g. $4.77), calculated by adding together the amount of tax owed plus the total cost of all shopping cart items.
    total=total_price + tax
    print("TOTAL AMOUNT OWED:", to_usd(total))

    # A friendly message thanking the customer and/or encouraging the customer to shop again.
    print("--------------------------------")
    print("Thanks for shopping at SAMS PLENTIFUL PRODUCE! Please come again!")