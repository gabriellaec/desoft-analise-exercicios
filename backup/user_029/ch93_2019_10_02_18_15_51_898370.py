x = 3435
def verifica_numero(x):
    lista = []
    soma = 0
    str(x)
    p = str(x)   
    z = p.split(" ")
    lista.append(z)
    soma = 0
    if x < 1:
        return False
    for i in range(len(lista)):
        soma+= i**i
        if soma == x:
            return True
        else: 
            return False
        