def classifica_lista(n):
    for i in n:
        if n[i-1]<n[i]:
            print ('crescente')
        if n[i-1]>n[i]:
            print ('decrescnete')
        if n[i-1]==n[i]:
            print ('nenhum')
        if n[i-1]==n[]:
            print ('nenhum')