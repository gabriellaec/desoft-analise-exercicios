def soma_valores(i):
    lista = [2,5,7,8,5,13,17,20]
    soma = 0
    i = 0
    while i <= len(lista-1):
        soma = soma + lista[i]
        i = i + 1
    print (soma)