def calcula_media(l):
    soma = 0
    divisor = 0
    for dic in l:
        for v in dic.values():
            soma += v
            divisor += 1
    return soma/divisor