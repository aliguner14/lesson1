from pprint import pprint
product = {
"name": "iPhone 12" , "price": 65432.1
}
phones = ["samsung Galaxy S21", "iPhone12"]
product["recomended"] = phones
pprint(product)
print(product["recomended"])
product["recomended"].append("Xiaomi Mi11")
print(len(product["recomended"]))
print(product["recomended"][0])
print("............................")
stock = [
    {"name": "iPhone 12 Plus", "stock": 24, "price": 65432.1,
    "recomended": ["Samsung Galaxy S21", "iPhone 12"]},
    {"name": "Samsung Galsxy S21", "stock": 8, 
    "price": 50000.0, "discount": 5000},
    {"name": "Xiaomi Mi11", "stock": 42, "price": 30000.5}
]
print(type(stock))
print(type(stock[0]))
print(stock[2])