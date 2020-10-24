retorno = []
def numero_no_indice(l):
    i = 0
    while i <= len(l):
        if l[i] == i:
            retorno.append(int(i))
            i +=1
        else:
            i +=1