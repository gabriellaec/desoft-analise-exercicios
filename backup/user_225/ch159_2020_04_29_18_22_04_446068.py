import json
with open("estoque.json", "r") as arquivo_json:
    texto = arquivo_json.read()
    dicionario = json.loads(texto)
    valortotal = 0
    for i in dicionario["produtos"]:
        a = int(dicionario["produtos"]["quantidade"])
        b = float(dicionario["produtos"]["valor"]
        valortotal+=a*b
    print(valortotal)
    