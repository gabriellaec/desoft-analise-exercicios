def apaga_repetidos(string):
    nova=""
    for i in string:
        if i not in nova:
            nova=nova+i
        else:
            nova=nova+'*'
    return nova