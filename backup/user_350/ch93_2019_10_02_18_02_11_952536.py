def verifica_munchhausen(n):
    numero = str(n)
    soma = 0 
    i=0
    while i < len(numero):
        soma += int(numero[i])**int(numero[i])
        i+=1
    if soma == n:
        return True
    else:
        return False 
    if n<1:
        return False
print(verifica_munchhausen(1))