def apaga_repetidos(texto):
    novo=''
    for i in texto:
        if i not in novo:
            novo=novo+i
        else:
            novo=novo+"*"
    return novo

        