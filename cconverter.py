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
cache["usd"] = load_rate(url, "usd")
cache["eur"] = load_rate(url, "eur")
while True:
    code_out = input().lower()
    if not code_out:
        break
    sum_in = input()
    if not sum_in.isnumeric():
        break
    sum_in = float(sum_in)
    print("Checking the cache...")
    if code_out in cache:
        print("Oh! It is in the cache!")
    else:
        print("Sorry, but it is not in the cache!")
        cache[code_out] = load_rate(url, code_out)
    rate = cache[code_out]["rate"]
    code = cache[code_out]["code"]
    sum_out = round(sum_in * rate, 2)
    print(f"You received {sum_out} {code}.")



