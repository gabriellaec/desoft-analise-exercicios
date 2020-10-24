
def soma_valores(lista):

    i = 0
    soma = 0

    while i < len(lista):
        soma = soma + lista[i]
        i += 1
    
    print(soma)


soma_valores([10, 15, 12])