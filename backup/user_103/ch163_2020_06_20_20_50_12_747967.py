def calcula_media(lista_notas):
    num=[]
    soma= 0 
    for i in range (len(lista_notas)):
        dicio = lista_notas[i]
        a= dicio.values()
        num.append(a)
    print(num)
    for j in range(len(num)):
        soma+= num[j]
    return soma/len(num) 
        