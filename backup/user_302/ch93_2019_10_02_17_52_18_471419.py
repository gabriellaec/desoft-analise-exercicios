def verifica_numero(numero):
    num = str(numero)
    num_algarismos = len(num)
    soma = 0
    if numero < 1:
        return False
    while num_algarismos > 0:
        soma += (int(str(numero[num_algarismos])))**(int(str(numero[num_algarismos])
        num_algarismos += -1
    if soma == numero:
        return True
    else:
        return False