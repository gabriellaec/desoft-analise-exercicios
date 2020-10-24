def faixa_notas(lista):
    lista_final=[]
    for nota in lista:
        if nota<5:
            y = lista.count(nota)
            lista_final.append(y)
        elif 5<=nota<=7:
            z = lista.count(nota)
            lista_final.append(z)
        else:
            w = lista.count(nota)
            lista_final.append(w)
            

    return lista_final
            