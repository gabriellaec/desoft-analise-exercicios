def remove_vogais(a):
    i = 0
    i_result = 0
    lista_resultado = []
    vogais = ['a', 'e', 'i', 'o', 'u']
    if a == 'aeiou':
        return []
    while i < len(a):
        if a[i] not in vogais:
            lista_resultado.append(a[i])
            i += 1
            i_result += 1
        else:
            i += 1
    n = 0
    resultado = ''
    while n < i_result:
        resultado += lista_resultado[n]
        n += 1
    
    
    return resultado 