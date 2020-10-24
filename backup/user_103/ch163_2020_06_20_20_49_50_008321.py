def calcula_media(lista_notas):
    num=[]
    soma= 0 
    for i in range (len(lista_notas)):
        dict = lista_notas[i]
        a= dict.values()
        num.append(a)
    print(num)
    for j in range(len(num)):
        soma+= num[j]
    return soma/len(num) 
        