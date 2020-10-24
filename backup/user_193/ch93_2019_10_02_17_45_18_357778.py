def verifica_numero(n):
    if n<1:
        return False
    i=0
    c=0
    z=str(n)
    while i<len(z):
        c=c+(int(z[i])**(int(z[i])))
        i+=1
    if n==c:
        return True