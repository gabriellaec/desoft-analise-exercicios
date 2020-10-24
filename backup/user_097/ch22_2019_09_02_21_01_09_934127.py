def eBissexto(ano):
    if (ano%100!=0) and (ano%4==0): #começar pelas exceçoes
        return False
    elif (ano%4==0):
        return True
    else:
        return False