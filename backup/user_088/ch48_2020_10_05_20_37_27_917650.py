def eh_crescente(a):
        i = 0
        resultado = True
    while i < len(a) - 1:
        if (a[i+1] > a[i]):
            resultado = True
            i += 1
        else:
            resultado = False
            break
        return resultado