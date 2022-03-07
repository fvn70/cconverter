import json
import requests
cache = {}

def load_rate(url, code):
    r = requests.get(url)
    rates = json.loads(r.text)
    c = code.lower()
    return rates[c] if c in rates else {}


code_in = input().lower()
url = f"http://www.floatrates.com/daily/{code_in}.json"
print(load_rate(url, "usd"))
print(load_rate(url, "eur"))
