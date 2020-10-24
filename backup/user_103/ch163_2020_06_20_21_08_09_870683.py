def calcula_media(lista_notas):
    lista_num =[]
    for i in range(len(lista_notas)):
        for nome,notas in lista_notas[i].items():
            a = lista_notas[i]
            a[nome] = notas
            lista_num.append(notas)
        print(lista_num)


        