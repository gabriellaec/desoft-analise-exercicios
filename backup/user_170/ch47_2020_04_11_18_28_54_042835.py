def estritamente_crescente(numeros):
    crescentes = []
    crescentes.append(numeros[0])
    for i in range(len(numeros)-1):
        if numeros[i+1] > numeros[i]:
            crescentes.append(numeros[i+1])
    return crescentes