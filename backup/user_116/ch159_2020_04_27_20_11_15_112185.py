import json
with open("estoque.json","r") as arquivo:
    texto=arquivo.read()
dicionario=json.loads(texto)
resultado=0
for ele in dicionario.values():
    for el in ele:
        resposta=el["quantidade"]*el["valor"]
        resultado+=resposta

print(resultado)