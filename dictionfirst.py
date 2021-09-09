product = {
"name": "iPhone 12" ,
"stock": 24 ,
"price": 65432.1
}
print(product)
product["memory"] = 128
print(product)
print(len(product))
print("name" in product)
print(product.get("name"))
print(product.get("discount", 123))
print(product)
del product["stock"]
print(product)