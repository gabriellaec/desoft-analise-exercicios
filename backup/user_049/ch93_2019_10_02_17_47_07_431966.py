def verifica_numero(n):
    if n < 1:
        return False
    if n >= 1:
        string=str(n)
        i=0
        s=0
        while i < len(string):
            numero=int(string[i])
            s+=numero**numero
            i+=1
        if n == s:
            return True
        if n!=1:
            return False