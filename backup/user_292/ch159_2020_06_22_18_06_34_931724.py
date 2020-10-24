import json 

with open('estoque.json', 'r') as arquivo:
    c = arquivo.read()
    e = json.loads(c)
    
    total = 0
    
    for i in e["produto"]:
        total += i["quantidade"] * i["valor"]
    print(total)