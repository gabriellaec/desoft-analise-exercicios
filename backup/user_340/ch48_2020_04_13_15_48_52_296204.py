def eh_crescente(lista):
    i=0
    s=0
    for t in lista:
        if t>s:
            s=t
        return True
        if t<s:
            return False
        
        