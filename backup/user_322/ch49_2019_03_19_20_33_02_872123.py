lista =[]
condicao = True
while condicao ==True:
    resposta =  int(input("escolha uma palavra:"))
    if resposta <= 0:
        condicao = False
    else:
        lista.append(resposta)
        condicao = True
tamanho = len(lista)
lista2 = []
i = 1
while i <=tamanho:
    lista2.append(lista[tamanho-i])
    i = i + 1
print(lista2)