import json
with open('estoque.json','r') as arq:
    cont = arq.read()

dic = json.loads(cont)

soma = 0
for e in dic:
    i = dic[e]
    for a in i:
        quant = a["quantidade"]
        val = a["valor"]
        total = quant*val
        soma += total
print(soma)