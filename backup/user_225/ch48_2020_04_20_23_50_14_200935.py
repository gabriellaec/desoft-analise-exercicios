def eh_crescente(lista):
    i = 1
    while i < len(lista):
        if lista[i] > lista[i -1]:
            m = 2
        else:
            m =3
            break
        i+=1
    if m==2:
        return True
    elif m==3:
        return False