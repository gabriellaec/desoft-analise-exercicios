i=0
def classifica_lista(n):
    if n[i-1]==[]:
            print ('nenhum') 
    for i in n:
        if n[i-1]<n[i]:
            print ('crescente')
        if n[i-1]>n[i]:
            print ('decrescnete')
        if n[i-1]==n[i]:
            print ('nenhum')