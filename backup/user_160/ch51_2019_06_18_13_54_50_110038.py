def estritamente_crescente(n):
    lista=[]
    if len(n) > 0:
        lista.append(n[0])
        maior = n[0]
    for i in n:
        if i > maior:
            maior = i
            print(maior)
            lista.append(i)
    return lista