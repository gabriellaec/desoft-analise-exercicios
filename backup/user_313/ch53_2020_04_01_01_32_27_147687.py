def soma_impares (l1):
    a = len(l1)
    contador = 0
    soma = 0

    while contador != a:
        
        if l1[contador]%2 != 0:
            soma = soma + l1[contador]
            contador = contador + 1

        else:
            contador = contador + 1

    return soma