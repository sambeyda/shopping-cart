#shopping_cart_test.py


from app.shopping_cart import to_usd, human_friendly_timestamp
import datetime
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