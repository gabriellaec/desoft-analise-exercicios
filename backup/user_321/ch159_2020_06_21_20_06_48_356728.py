import json 
with open ('estoque.json', 'r') as estoque:
    texto = estoque.read()
    
dicionario = json.loads(texto)
print (dicionario)