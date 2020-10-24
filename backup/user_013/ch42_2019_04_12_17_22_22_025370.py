def quantos_uns(n):
    resultado = 0
    m = str(n)
    for i in m:
        if i == '1':
            resultado += 1
    return resultado