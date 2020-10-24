import json
with open('estoque.json', 'r') as arquivo_json:
    texto = arquivo_json.read()
dicionario = json.loads(texto)

quantidades = []
valores = []
for qtde, val in dicionario.items():
    if qtd == "quantidade":
        quantidades.append(dicionario[qtd])
    if val == "valor":
        valores.append(dicionario[val])

dinheiro = []
i = 0
while i < len(quantidades):
    dinheiro.append(int(quantidades[i])*float(valores[i]))
    i+=1

print(sum(dinheiro))
