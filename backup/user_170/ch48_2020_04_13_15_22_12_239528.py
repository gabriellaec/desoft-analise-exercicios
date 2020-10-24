def eh_crescente(numeros):
    if len(numeros) > 0 :
        crescentes = []
        crescentes.append(numeros[0])
        m = numeros[0]
        for i in range(len(numeros)-1):
            if m < numeros[i+1]:
                m = numeros[i+1]
                crescentes.append(numeros[i+1])
        if crescentes == numeros:
            return True
        else:
            return False
    else:
        return True