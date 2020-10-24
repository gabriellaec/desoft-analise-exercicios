def faixa_notas(lista):
    lista_final=[]
    y = 0
    z = 0
    w = 0
    for nota in lista:
        if nota<5:
            y+=1    
        elif 5<=nota<=7:
            z+=1    
        else:
            w+=1
      
           
    lista_final = [y,z,w] 
    return lista_final
            