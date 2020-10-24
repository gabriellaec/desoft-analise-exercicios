def estritamente_crescente(lista):
    numero_atual = 0
    numero_anterior =0
    i=0
    nova_lista=[]
    while len(lista)>i:
        numero_atual=lista[i]
        if numero_atual>numero_anterior:
            numero_anterior=numero_atual
            nova_lista.append(numero_atual)
            i+=1
        else:
            i+=1
    return nova_lista