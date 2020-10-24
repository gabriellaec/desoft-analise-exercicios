import json

with open("estoque.json", "r") as arquivo_json:
    texto = arquivo_json.read()
    
dicionario_produtos = json.loads(texto)

lista_chave = dicionario_produtos["produtos"]

i = 0 

while i < len(lista_chave):
    conta = []
    quantidade = lista_chave[i]["quantidade"]
    valor = lista_chave[i]["valor"]
    conta.append(quantidade*valor)
    
    i+=1
print(sum(conta))

