def e_primo(p):
    if p < 2:
        return False
    for i in range(2, p):
        if p%i==0:
            return False
    return True
def primos_entre(a,b):
    lista=[]
    for i in range(a, b+1):
        if e_primo(i)==True:
            lista.append(i)
    return lista
