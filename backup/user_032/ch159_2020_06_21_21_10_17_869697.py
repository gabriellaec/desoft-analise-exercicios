import json
with open('estoque.json','r') as arquivo_json:
    texto = arquivo_json.read()
dicionario = json.loads(texto)
lista = []
for c,v in dicionario.items():
    lista.append(v)
t = 0
for dic in lista:
    for i in dic:
        print(i)
        valor = i['quantidade']*i['valor']
        t += valor
print(t)