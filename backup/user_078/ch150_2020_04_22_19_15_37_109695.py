def calcula_pi (n):
    lista = []
    for n in range (1, n+1):
        lista.append(6/(n**2))
    soma = sum(lista)
    return (soma)**5