def faixa_notas(lista):
    lista_final=[]
    for nota in lista:
        if nota<5:
            y = lista.count(nota)
            
        elif 5<=nota<=7:
            z = lista.count(nota)
            
        else:
            w = lista.count(nota)
      
            
    lista_final = [y,z,w] 
    return lista_final
            