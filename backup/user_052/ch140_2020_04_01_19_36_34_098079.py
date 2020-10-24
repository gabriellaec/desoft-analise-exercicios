def faixa_notas (lista):
    lista_notas=[0]*3
    a=len(lista)
    i=0
    x=0
    y=0
    z=0
    lista_notas[0]=x
    lista_notas[1]=y
    lista_notas[2]=z
    lista_notas=[x,y,z]
    while i<a:
        if lista[i]<5:
            x+=1
        elif 5<=lista[i]>=7:
            y+=1
        else:
            z+=1
    return lista_notas
            
    