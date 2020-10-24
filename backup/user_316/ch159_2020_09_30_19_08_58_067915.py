import json

final_price = 0

with open('estoque.json', 'r') as file:
    content = file.read()
    
dc = json.loads(content)
for e in dc["produtos"]:
    final_price += float(e["quantidade"]) * float(e["valor"])
    
print(final_price)