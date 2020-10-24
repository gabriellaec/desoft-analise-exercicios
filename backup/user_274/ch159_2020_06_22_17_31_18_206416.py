import json
t = 0

with open("estoque.json", "r") as estoque:
    arq = estoque.read()
    dicio = json.loads(arq)
    for i in dicio.items():
        q = i["quantidade"]
        p = i["valor"]
        t = t + q*p
print(t)
    