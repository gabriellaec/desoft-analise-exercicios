def verifica_progressao (lista):
    for i in lista:
        if lista[0] == lista[2] - lista[1]:
            return "PA"
        elif lista[0] == lista[2]/lista[1]:
            return "PG"
        elif lista[0] == 0 and lista[1] == 0:
            return "AG"
        elif lista[0] == 1 and lista[1] == 1:
            return "AG"
        
        
        