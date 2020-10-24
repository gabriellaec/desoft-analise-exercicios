import json
t = 0

with open("estoque.json", "r") as estoque:
    arq = estoque.read()
    dicio = json.loads(arq)
    for a in dicio["produtos"]:
        t = t + a["quantidade"] * a["valor"]
        
print(t)
    