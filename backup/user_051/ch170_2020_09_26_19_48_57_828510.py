def apaga_repetidos(stri):
    rep=''
    for i in stri:
        if i not in rep:
            rep+=i
        else:
            rep+='*'
    return rep