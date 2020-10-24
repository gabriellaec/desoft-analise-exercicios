def posicoes_minusculas (s):
    lista = list(s)
    lista_2 = []
    num = 0
    for i in lista:
        if i.islower():
            lista_2.append(num)
        num+= 1 
            
    return(lista_2)