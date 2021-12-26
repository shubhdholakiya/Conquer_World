from forex_python.converter import CurrencyRates, CurrencyCodes
from forex_python.bitcoin import BtcConverter

c = CurrencyRates()
curr = CurrencyCodes()
# print(curr.get_symbol("INR"))

# print(c.get_rate("INR", "USD"))

# print(c.convert("USD", "INR", 20))


b = BtcConverter()
print(b.get_latest_price("INR"))
