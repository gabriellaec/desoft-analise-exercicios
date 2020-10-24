import json
with open("estoque.json", "r") as arquivo_json:
    texto = arquivo_json.read()
    dicionario = json.loads(texto)
    valortotal = 0
    for i in dicionario["produtos"]:
        valortotal+= int (dicionario["produtos"]["quantidade"])*float (dicionario["produtos"]["valor"])
    print(valortotal)
    