def quantos_uns(n):
    conta_um = 0
    while n > 0:
        resto = n % 10
        if resto == 1:
            conta_um += 1
        n = n // 10
    return conta_um