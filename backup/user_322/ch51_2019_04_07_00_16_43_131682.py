def estritamente_crescente(n):
    lista=[]
    for i in n:
        lista.append(n[0])
        maior = n[0]
        if i > maior:
            maior = i
            print(maior)
            lista.append(i)
    return lista