def calcula_fibonacci (numero):
    lista= [1,1]
    i = 1
    soma=0
    if numero == 1:
        print ([1])
    while i < (numero-1):
        soma = lista[i] + lista[i-1]
        lista.append (soma)
        i += 1
    return lista