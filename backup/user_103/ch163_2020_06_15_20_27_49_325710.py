def calcula_media(lista_notas):
    soma=0
    lista_num=[]
    for i in range (len(lista_notas)):
        a= lista_notas[i]
        num= lista_notas[i].values
        lista_num.append(a)
        print(lista_num)
    for j in range(len(lista_num)):
        soma += lista_num[i]
    return soma/(len(lista_num)+1)