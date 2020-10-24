def verifica_numero(n):
    i = 0
    for i in len(n):
        if i == i + i**i:
            return True
        elif i < 1:
            return False
        else:
            return False
            
            
            
    