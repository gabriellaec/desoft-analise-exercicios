def estritamente_crescente(a):
    i = 1
    indice_resultado = 0
    if len(a) != 0:
        resultado = [a[0]]
    else:
        return []
    while i < len(a):
        if a[i] > resultado[indice_resultado]:
            resultado.append(a[i])
            i += 1
            indice_resultado += 1
            
        else:
            i += 1
            
    return resultado
print(estritamente_crescente([10, 15, 13, 12, 14]))