lista = []
condicao = True
while condicao == True:
    resposta = input("escolha uma palavra:")
    lista.append(resposta)
    if resposta == "fim":
        condicao = False
    else:
        condicao = True
tamanho = len(lista)
i=0
lista_final = []
while i< tamanho-1:
    if lista[i][0] == "a":
        lista_final.append(lista[i])
        i=i+1
    else:
        i=i+1
print(lista_final)        
       