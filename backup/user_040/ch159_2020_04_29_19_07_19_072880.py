import json

with open("estoque.json") as arquivo:
    texto = arquivo.read()
    conteudo = json.loads(texto)
    valor_total = 0
    for x, y in conteudo.items():
        for z in y:
            for h in z:
                quantidade = int(h[1])
                valor = int(h[2])
                valor_total += quantidade*valor
print (valor_total)