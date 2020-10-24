def verifica_numero(n):
    a=str(n)
    lista=[]
    listaquadrados=[]
    for e in a:
        lista.append(e)
    for i in lista:
        b=int(i)
        c=(b**b)
        listaquadrados.append(c)
    soma=0
    for f in listaquadrados:
        soma=soma+f
    if soma==n:
        return True
    elif n<1:
        return False
    else:
        return False