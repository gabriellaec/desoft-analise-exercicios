import json
with open ("estoque.json", "r") as arquivo:
    ler = arquivo.read()
    dic = json.loads(ler)
    valor_total = 0
    for i in dic:
        for e in dic[i]:
            valor_total += e["quantidade"] * e["valor"]
    print(valor_total)
            