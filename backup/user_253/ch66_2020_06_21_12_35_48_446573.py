def lista_sufixos (string):
    lista = string.split()
    numero = list(string)
    h= len(numero)
    i=0
    b=[]
    while i < h:
        b.insert(i, lista)
        lista.pop(i)
        i+=1
    return b