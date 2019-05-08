#shopping_cart_test.py


from app.shopping_cart import to_usd, human_friendly_timestamp, find_product
import datetime
import pytest
#Basic Challenge
def test_to_usd():
    #Tests whether number is returned with $ sign and two decimal places
    assert to_usd(10) == "$10.00"

    #Tests whether number rounds decimal places
    assert to_usd(10.33333333333333) == "$10.33"

    #Tests whether there is a thousand seperator
    assert to_usd(10000) == "$10,000.00"
#Basic Challenge
def test_human_friendly_timestamp():
    #Tests whether checkout time date and time is displayed properly
    assert human_friendly_timestamp(datetime.datetime.now()) == datetime.datetime.now().strftime("%m-%d-%Y %I:%M %p")
#Intermediate Challenge
def test_get_product():
    #Tests whether product identifier works correctly for all categories
    products= [
        {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
        {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
        {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50}
    ]
    #def find_product(selected_id, products):
    #selected id, products
    #Ensure result is correct
    matching_product = find_product("5", products)
    assert matching_product["name"]== "Green Chile Anytime Sauce"
    assert matching_product["department"]== "pantry"
    assert matching_product["aisle"]== "marinades meat preparation"
    assert matching_product["price"]== 7.99
    #Ensure error is processed when ID doesn't exist
    #Adapted from professor and: https://docs.pytest.org/en/latest/assert.html
    with pytest.raises(IndexError):
        find_product("50", products)
    



