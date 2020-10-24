def eh_primo(numero):

# Divisores --------------------------

    lista_de_divisores = [2]

    for indice in range(3, numero, 2):
        lista_de_divisores.append(indice)
    lista_de_divisores.append(numero)

# Divisores --------------------------

# Processo de Divisão ----------------

    divisores_r_0 = [1]
    divisores_r_dif_0 = []

    for divisor in lista_de_divisores:
        if numero % divisor == 0:
            divisores_r_0.append(divisor)
        else:
            divisores_r_dif_0.append(divisor)

# Processo de Divisão ----------------

# Verifica Resultados ----------------
    
    lista_verifica_primo = [1, numero]

    if divisores_r_0 != lista_verifica_primo:
        resultado = False
        print('O número {} não é primo.'.format(numero))
    else:
        resultado = True
        print('O número {} é primo.'.format(numero))

# Verifica Resultados ----------------

    return resultado

eh_primo(23)