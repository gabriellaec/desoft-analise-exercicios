
def numero_no_indice(lista):
    novalista = []
    t=0
    while t<len(lista):
        if lista[t]==t:
            novalista.append(lista[t])
            t+=1
        else:
            t+=1
    return novalista

            
        
    