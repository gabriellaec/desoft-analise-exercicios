def estritamente_crescente(numeros):
    if len(numeros) > 0 :
        crescentes = []
        crescentes.append(numeros[0])
        m = numeros[0]
        for i in range(len(numeros)-1):
            if numeros[m] > numeros[i]:
                m = nuemros[i]
                crescentes.append(numeros[i])
                
        return crescentes
    else:
        return []

print(estritamente_crescente([10, 15, 11, 12, 13, 14]))