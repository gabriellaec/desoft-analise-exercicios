import json
with open('estoque.json', 'r') as arquivo_j:
    texto = arquivo_j.read()

dic = json.loads(texto)
total = 0
for k in dic:
    q = k["quantidade"]
    total += q
print(total)