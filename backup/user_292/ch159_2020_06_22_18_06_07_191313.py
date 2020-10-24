import json 

with open('estoque.json', 'r') as arquivo:
    c = arquivo.read()
    e = json.loads(c)
    
    total = 0
    
    for i in e["p"]:
        total += i["q"] * i["v"]
    print(total)