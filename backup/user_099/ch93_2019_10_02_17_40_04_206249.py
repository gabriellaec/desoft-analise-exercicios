def verifica_numero(numero):
    numero_valor=int(numero)
    if numero_valor<1:
        return False
    else:
        numero_digitos=str(numero)
        soma=0
        for digito in numero_digitos:
            soma+=int(digito)**int(digito)
        if numero_valor==soma:
            return True
        else:
            return False