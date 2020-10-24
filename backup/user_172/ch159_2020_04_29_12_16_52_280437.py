import json
with open ('estoque.json', 'r') as arquivo:
    conteudo = arquivo.read()
    
dicionario = json.loads(conteudo)
soma = 0
lista = dicionario ['produtos'] 
i = 0
while i <len(lista):
    dicio = lista[i]
    a = dicio['quantidade']
    b = dicio['valor']
    soma = soma + a*b
    i+=1
        
print(soma)