def soma_valores(lista_n):
    soma = 0
    i = 1
    while i <= len(lista_n):
        soma = lista_n[i] + lista_n[i - 1]
        i += 1
        
    return soma