def eh_crescente(lista):
    if lista==[] or len(lista)==1:
        return False
    i=1
    u=0
    while i<=len(lista):
        while lista[u]<lista[i]:
            u+=1
            i+=1
        if i==len(lista):
            return True
        else:
            return False

