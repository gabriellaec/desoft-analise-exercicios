def classifica_lista(n1,n2,n3):
    n1=int(input('me de um numero'))
    n2=int(input('me de um número')) 
    n3=int(input('me de um numero'))
    if n1<n2<n3:
        print ('crescente')
    elif n1>n2>n3:
        print ('decrescente')
    else:
        print ('nenhum')