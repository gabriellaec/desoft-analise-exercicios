def verifica_numero(numero):
    numero_stringado = str(numero)
    i = 0
    soma = 0
    if numero < 1: 
        return False
    elif numero >= 0:
        while i < len(numero_stringado):
            numeral = int(numero_stringado[i])
            quadrado_do_numero = numeral ** numeral
            soma = soma + quadrado_do_numero
            i = i + 1
        if soma == numero:
            return True
        else:
            return False