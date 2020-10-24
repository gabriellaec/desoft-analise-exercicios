import json

with open("estoque.json") as arquivo:
    texto = arquivo.read()
    conteudo = json.loads(texto)
    valor_total = 0
    for x, y in conteudo.items():
        for z in y:
            for a, b in z.items:
                if "quantidade" in a:
                    quantidade = b
                elif "valor" in a:
                    valor = b
                    valor_total += quantidade*valor
print (valor_total)