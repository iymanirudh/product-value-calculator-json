import json
# Create products.json (so the program runs on any online compiler)
data = [
  {"ProductID": 1, "Product": "Laptop",   "Quantity": 2, "Price": 45000},
  {"ProductID": 2, "Product": "Mouse",    "Quantity": 5, "Price": 500},
  {"ProductID": 3, "Product": "Keyboard", "Quantity": 3, "Price": 1200},
  {"ProductID": 4, "Product": "Monitor",  "Quantity": 2, "Price": 12000}
]
with open("products.json", "w") as f:
  json.dump(data, f, indent=2)
# Read the JSON file and calculate total value of each product
with open("products.json", "r") as file:
  products = json.load(file)

for item in products:
  total = item["Quantity"] * item["Price"]
  print(f"{item['Product']}: {total}")
