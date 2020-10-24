def quantos_uns(numero):
    numero=input('Digite um numero:')
    i=0
    primeiro_numero=numero[i]
    while primeiro_numero!=1:
        i+=1
    if primeiro_numero==1:
        lista=primeiro_numero
        a=len(lista)
        print(a)
        