def verifica_numero(n): 
    soma = 0
    a = n 
    b = str(a) 
    for i in range(len(b)):
        soma += int(b[i]**2)
        if soma == n:
            return True
        else: 
            return False 