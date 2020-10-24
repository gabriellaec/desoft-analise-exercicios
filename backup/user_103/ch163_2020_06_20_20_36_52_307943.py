def calcula_media(lista_notas):
    soma=0
    lista_num=[]
    for i in range (len(lista_notas)):
        num= lista_notas[i].value
        lista_num.append(num)
        print(lista_num)
    for j in range(len(lista_num)):
        soma += lista_num[i]
    return soma/(len(lista_num)+1)