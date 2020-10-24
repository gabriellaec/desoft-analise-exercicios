def faixa_notas(lista):
    lista_final=[]
    a = 0
    b = 0
    c = 0
    for nota in lista:
        if nota<5:
            a+=1
            lista_final.append(a)
        elif 5<=nota<=7:
            b+=1
            lista_final.append(b)
        else:
            c+=1
            lista_final.append(c)
    return lista_final
            