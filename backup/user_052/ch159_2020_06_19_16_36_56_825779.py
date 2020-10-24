import json

with open ("estoque.json", "r") as arquivo:
    x = arquivo.read()
    v = json.loads(x)    #padrão para ler json
    soma = 0
    for i in v["produtos"]:
        soma += i["quantidade"] * i["valor"]
    return soma
        
                
        
        