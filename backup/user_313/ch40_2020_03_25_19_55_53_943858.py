def soma_valores(lista):
    a = len(lista)
    indice = 0
    soma = 0
    while indice < a:
        soma = soma + lista[indice]
        indice = indice + 1
    return(soma)