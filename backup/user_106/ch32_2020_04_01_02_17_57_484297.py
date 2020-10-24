def lista_primos(n):
    lista=[]
    n=len(lista)
    i=0
    a=0
    def eh_primo(x):
        if x==0:
            return False
        elif x==1:
            return False
        elif x==2:
            return True
        elif x%2==0:
            return False
        else:
            i=3
            while i<x:
                if x%i==0:
                    return False
                i+=2
            return True
    while i<n:
        if eh_primo(a):
            a=lista[i]
            lista.append(a)
            i+=1
        a+=1
    return lista
    
g=int(input('Digite um número: '))
print(lista_primos(g))