def estritamente_crescente(n):
    lista=[]
    lista.append(n[0])
    maior = n[0]
    for i in range(1, len(n)):
        if n[i] > maior:
            maior = n[i]
            lista.append(n[i])
    return lista