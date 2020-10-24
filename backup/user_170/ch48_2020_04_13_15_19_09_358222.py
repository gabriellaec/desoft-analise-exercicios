def eh_crescente(numeros):
    crescentes = []
    m = numeros[0]
    crescentes.append(m)
    for i in range(len(numeros)-1):
        if m < numeros[i+1]:
            m = numeros[i+1]
            crescentes.append(numeros[i+1])
    if crescentes == numeros:
        return True
    else:
        return False