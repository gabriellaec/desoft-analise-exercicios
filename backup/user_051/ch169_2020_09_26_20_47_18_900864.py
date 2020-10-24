def login_disponivel(stri, lista):
    if stri != 'fim':
        if stri not in lista:
            lista.append(stri)
        else:
            i=1
            x=stri+str(i)
            while x in lista:
                x=stri+str(i)
                i+=1
            lista.append(x)
stri=input('login novo: ')
lista=[]
q=login_disponivel(stri, lista)
f='fim'
while stri!= f:
    stri=input('login novo: ')
    q=login_disponivel(stri, lista)
i=0

while i<len(lista):
    a=lista[i]
    print(a)
    i+=1