from forex_python.converter import CurrencyRates, CurrencyCodes
from forex_python.bitcoin import BtcConverter

c = CurrencyRates()
curr = CurrencyCodes()
# print(curr.get_symbol("INR")) # Print the Symbol of given currency.

# print(c.get_rate("INR", "USD")) # Print rate of first currency in terms of second currency.

# print(c.convert("USD", "INR", 20)) # Convert given amount from one curreny to another.


b = BtcConverter()
print(b.get_latest_price("INR")) # Print rate of BTC in INR.
