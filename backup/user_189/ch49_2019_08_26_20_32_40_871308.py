def inverte_lista(lista):
    n=1
    while n>0:
        n=int(input("digite um numero inteiro e positivo: "))
        lista.append(n)
    a=(len(lista)-1)
    resp=[]
    while a>=0:
        b=lista[a]
        resp.append(b)
        a-=1
    return resp
lista=[]
print(inverte_lista(lista))       
        
        
        