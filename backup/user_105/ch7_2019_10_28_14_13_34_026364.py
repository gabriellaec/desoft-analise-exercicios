def calcula_norma(lista):
    x = lista[0]
    if len(lista)>1:
        y = lista[1]
        modulo = (((x)**2)+((y)**2))**(1/2)
    else:
        modulo = abs(x)      
               
    return modulo