def verifica_numero(numero):
    num_algarismos = int(len(numero))
    soma = 0
    if int(numero) < 1:
        return False
    while num_algarismos > 0:
        soma += (numero[num_algarismos])**numero[num_algarismos]
        num_algarismos -= 1
    if soma == numero:
        return True
    else:
        return False