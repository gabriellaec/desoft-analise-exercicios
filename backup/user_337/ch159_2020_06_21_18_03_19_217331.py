import json
with open('estoque.json', 'r') as arquivo_json:
    texto = arquivo_json.read()
dic = json.loads(texto)
lista= []
for produto in dic:
    for a in dic[produto]:
        for b in a.values():
            lista.append(b)
valor = 0 
print(lista)
i = 0
while i < len(lista)-1:
    valor += lista[i+1]*lista[i+2]
    i+=3
print(valor)