def eh_primo(numero):
    inicio = 1
    contar_divisores = 0
    while inicio<=numero:
        if numero%inico==0:
            contar_divisores +=1
        inicio = inicio + 1
    if contar_divisores > 2:
        return False
    else:
        return True
