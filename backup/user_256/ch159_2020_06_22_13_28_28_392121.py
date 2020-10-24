import json
with open("estoque.json", "r") as arquivo_json:
    texto=arquivo_json.read()
dicionario=json.loads(texto)
lista = dicionario["produtos"]
valor_lista=[]
for dic in lista:
    valor = dic