def apaga_repetidos (frase):
    letras=[]
    nova=''
    for c in frase:
        if c not in letras:
            letras.append(c)
            nova+=c
        else:
            nova+='*'
    return nova