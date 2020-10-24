def eh_crescente(lista):
    v=0
    a=True
    for i in lista:
        if i>v:
            v=i
        else:
            return False
      