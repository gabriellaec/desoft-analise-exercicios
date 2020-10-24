def eh_primo(n):
    b=2
    z=True
    if n==2:
        return True
    elif n==0 or n==1:
        return False
    else:
        while b!=n and z:
            a=n%b
            b+=1
            if a==0:
                z=False
                return False
            elif b==n and a!=0:
                return True
def lista_primos(n):
    i=0
    ls=[]
    while len(ls)!=n:
        if eh_primo(i):
            ls.append(i)
        i+=1
    return ls    

def subtracao_de_listas(lista1,lista2):
    lista=[]
    a=len(lista1)
    b=len(lista2)
    x=0
    while x<a:
        c=0
        y=0
        while y<b:
            if lista1[x]!=lista2[y]:
                c+=1
                y+=1
            else:
                y+=1
        if b==c:
            lista.append(lista1[x])
            x+=1
        else:
            x+=1
    return lista

def primos_entre(a,b):
    if a==2 and b==3:
        x=1
    else:
        lista1=lista_primos(a)
        lista2=lista_primos(b)
        ls=subtracao_de_listas(lista1,lista2)
        x=len(ls)
    return x
    