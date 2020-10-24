def verifica_numero(numero):
    soma = 0
    i = 0

    if numero < 0:
        return False
    else:
        string_numero = str(numero)
        while i < len(string_numero):
            valor_string = string_numero[i]
            valor_operacao = int(valor_string)
            conta = valor_operacao**valor_operacao
            soma = soma + conta
            i += 1

        if soma == numero:
            return True
        else:
            return False