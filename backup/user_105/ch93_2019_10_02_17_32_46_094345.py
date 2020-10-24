def num_munch(numero):
    if numero < 0:
        return False
    else:
        n = numero
        x = str(numero)
        soma = 0
        i = 0
        while i < len(x):
            inteiro = int(x[i])
            soma = soma + inteiro**inteiro
            i+=1
        if n < 1:
            return False
        else:
            return n==soma 