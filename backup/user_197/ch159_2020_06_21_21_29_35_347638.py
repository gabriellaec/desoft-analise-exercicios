import json

with open ("estoque.json", "r") as arquivo:
    ler = arquivo.read()
    dic = json.loads(ler)
    valor_total = 0
    for i in dic:
        for e in dic[i]:
            if e == float(dic[i]):
                valor_total += 1
    print(valor_total)
    