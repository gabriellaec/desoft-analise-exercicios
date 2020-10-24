def encontra_maximo(lista):
    i=0
    lista_final1=[]
    lista_final2=[]
    lista_final3=[]
    while i<3:
        lista_final1=lista[:1]
        lista_final2=lista[1:2]
        lista_final3=lista[2:3]
        i+=1
    lista_final=[]
    p=0
    while p<3:
        lista_final.extend(max(lista_final1))
        lista_final.extend(max(lista_final2))
        lista_final.extend(max(lista_final3))
        p+=1
    return (lista_final)