import json
with open ("estoque.json","r") as arquivo:
    texto = arquivo.read()
    dicionario = json.loads(texto)

    total = 0
    for preço in dicionario["produtos"]:
        total += preço["quantidade"] * preço["valor"]
    print total