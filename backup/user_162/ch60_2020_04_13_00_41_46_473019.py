def eh_palindromo(a):
    inverso = []
    na = []
    for i in a:
        inverso.insert(0, i)
        na.append(i)    
    if inverso == na:
        return True
    else:
        return False