import json
with open('estoque.json', 'r') as arquivo_json:
    texto = arquivo_json.read()

dicionario1 = json.loads(texto)
lista_produtos = dicionario1["produtos"]

quantidades = []
valores = []
i = 0
while i<len(lista_produtos):
    for qtde, val in lista_produtos[i].items():
        if qtde == "quantidade":
            quantidades.append(lista_produtos[i][qtde])
        if val == "valor":
            valores.append(lista_produtos[i][val])

dinheiro = []
i = 0
while i < len(quantidades):
    dinheiro.append(int(quantidades[i])*float(valores[i]))
    i+=1

print(sum(dinheiro))
