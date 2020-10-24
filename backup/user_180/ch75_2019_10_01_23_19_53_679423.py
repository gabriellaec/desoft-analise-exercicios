def verifica_primos(lista_numeros):
    dicionario_primo = {}
    for numero in lista_numeros:
        if numero > 1:
            for i in range(2, numero):
                if numero % 2 == 0:
                    dicionario_primo[numero] = False
            else:
                dicionario_primo[numero] = True
        else:
            dicionario_primo[numero] = False
    return dicionario_primo