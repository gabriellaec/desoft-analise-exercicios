def login_disponivel(N,L):
    i=0
    while i<len(L):
        if N not in L:
            L.append(N)
        elif N+str(i) not in L:
            L.append(N+str(i))
        else:
            i+=1
 #roda bem mais do que o necessario, porem eh impossivel ter um nome de usuario maior que o tamanho da lista, portanto tambem funciona