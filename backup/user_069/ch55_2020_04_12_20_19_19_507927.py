def encontra_maximo (matriz):
    lista_final = []
    for lista in matriz:
        for e in lista:
            lista_final.append(abs(e))    
    return (max(lista_final))