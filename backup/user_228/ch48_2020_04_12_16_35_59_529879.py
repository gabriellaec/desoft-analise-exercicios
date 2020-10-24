def eh_crescente(lista):
    v=0
    a=True
    while a:
        for i in lista:
            if i>v:
                v=i
            else:
                a=False
                
    return a