def faixa_notas(lista_notas):
    x=0
    y=0
    z=0
    l3=[x,y,z]
    lista_counter=0
    while lista_counter<len(lista_notas):
        if lista_notas[lista_counter]<5:
            x+=1
            lista_counter+=1
        if 5<=lista_notas[lista_counter]<=7:
            y+=1
            lista_counter+=1
        if lista_notas[lista_counter]>7:
            z+=1
            lista_counter+=1
        return l3