def primo(p):
    if p >1:
        for x in range (2,p):
            if p%x == 0:
                return False
    else:
        return False
    return True

def primos_entre(a,b):
    lista=[]
    i=a
    while i <= b:
        primos=primo(i)
        if primos:
                lista.append(i)
        i+=1
    return len(lista)


print(primos_entre(1,10))