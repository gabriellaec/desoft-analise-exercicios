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
    i+=1

dinheiro = [0]*len(valores)
j = 0
while j<len(valores):
    dinheiro[j] = int(quantidades[j])*float(valores[j])
    j+=1
