def calcula_total_da_nota(lista,lista2):
    i=0
    lista3=[]
    while i <len(lista):
        lista3.append(lista[i]*lista2[i])
     
        i+=1
    return sum(lista3)

    