with open('estoque.json', 'r') as e:
    estoque = e.read()
dicio = json.loads(estoque)
total = 0
for i in dicio:
    q = i[quantidade]
    v = i[valor]
    total += q*v
print(total)
    