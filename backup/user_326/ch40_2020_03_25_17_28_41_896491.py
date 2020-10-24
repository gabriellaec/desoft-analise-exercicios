def soma_valores(lista):
    n_elementos = len(lista) - 1 
    soma = 0
    while n_elementos >= 0:
        soma = soma + lista[n_elementos]
        n_elementos -= 1