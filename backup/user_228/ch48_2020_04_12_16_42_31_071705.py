def eh_crescente(lista):
    v=0
    for i in lista:
        if i>v:
            v=i
            return True
        else:
            return False
                