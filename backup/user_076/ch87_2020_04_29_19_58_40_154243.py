with open('churras.txt','r') as arquivo:
    lista_linhas = arquivo.readlines()
    valor=0
    for i in lista_linhas:
        i.split(',')
        valor += float(lista_itens[i][1]) * float(lista_itens[i][2])
print(valor)