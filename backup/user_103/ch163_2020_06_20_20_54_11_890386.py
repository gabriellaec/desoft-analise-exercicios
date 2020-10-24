def calcula_media(lista_notas):
    num=[]
    soma= 0 
    for i in range (len(lista_notas)):
        for valores in lista_notas[i]:
            a= lista_notas[valores]
            num.append(a)
        print(num)

        