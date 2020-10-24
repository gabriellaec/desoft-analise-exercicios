import json
with open ('estoque.json', 'r') as arquivo_json:
    texto = arquivo_json.read()
    
    dicionario = json.loads(texto)
    for valores in dicionario.values():
        i = 1
        while i < 3:
            k+=dicionario[i]*dicionario[i+1]
        print (k)