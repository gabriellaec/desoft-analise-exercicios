def estritamente_crescente(numeros):
    if len(numeros) > 0 :
        crescentes = []
        crescentes.append(numeros[0])
        for i in range(len(numeros)-1):
            if numeros[i+1] > numeros[i] and numeros[i+1] > numeros[i-n]:
                crescentes.append(numeros[i+1])
                
        return crescentes
    else:
        return []

print(estritamente_crescente([10, 15, 11, 12, 13, 14]))