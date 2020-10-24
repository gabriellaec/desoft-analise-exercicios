
def calcula_fibonacci (numero):
    lista= [1]
    i = 0
    soma=0
    while i < (numero-1):
        soma = lista[i] + lista[i-1]
        lista.append (soma)
        i += 1
    return lista