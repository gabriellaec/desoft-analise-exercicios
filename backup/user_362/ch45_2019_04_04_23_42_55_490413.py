def zera_negativos(valores):
    valores_pos=[]
    i=0
    while i<len(valores):
        if valores[i] < 0:
            valores_pos.append(valores[i])
        i+=1
    return valores_pos
        
    