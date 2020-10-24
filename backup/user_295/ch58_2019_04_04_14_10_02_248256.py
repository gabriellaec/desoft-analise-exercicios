
def calcula_fibonacci (numero):
    lista= [1,1]
    i = 1
    soma=0
    while i < (numero):
        soma = soma + lista[i] + lista[i-1]
        lista.append (soma)
        i += 1
    return lista

