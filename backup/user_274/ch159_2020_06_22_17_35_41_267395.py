import json
t = 0
q = 0
p = 0

with open("estoque.json", "r") as estoque:
    arq = estoque.read()
    dicio = json.loads(arq)
    for i,j in dicio.items():
        if i == "quantidade":
            q = j
        elif i == "valor":
            p = j
        t = t + q*p
print(t)
    