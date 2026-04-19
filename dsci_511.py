print ("Running test.py")
x = 10** - 2
print("Result is", x)

###2026-04-19
### Set : {}, un-ordered list of unique itmes

penguins = {"Gilbert", "Gertrude", "Gretta", "Gilbert"}
print(penguins)

### Immutable: () - tuple
### Mutable: []

name = "Hyungtae"
age = 32 + 16/365
template_new = f'Hello, my name is {name} and I am {age:.2f} years old.'
print(template_new)

### Dictionary

house = {'bedrooms': 3, 'bathrooms': 2, 'square_feet': 2000, 'city': 'Newmarket', 'price': 500000}
condo = {'bedrooms': 2, 'bathrooms': 1, 'square_feet': 1000, 'city': 'Toronto', 'price': 300000}
print(house['bedrooms'])

house['bedrooms'] = 55
print(house['bedrooms'])

del house['square_feet']
print(house)

### Set default values
print(condo.get("bedrooms", "Key not found"))
print(condo.get("fireplaces", "Key not found"))

### Inline if/else
penguins = ["Gilbert", "Gertrude", "Gretta", "Gus Gus", "Guin", "Fetti"]
x = "get more penguins" if len(penguins) < 5 else "No more penguins needed"
print(x)