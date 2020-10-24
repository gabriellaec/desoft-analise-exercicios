def verifica_numero(n):
    i = 0
    s = 0
    n1 = str(n)
    if n < 1:
        return False
    while i < len(n1):
        a = int(n1[i])**int(n1[i])
        s+=a
        i+=1
    if s == n:
        return True
    else:
        return False 