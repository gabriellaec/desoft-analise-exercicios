def capitaliza(palavra):
    letra=palavra[0].upper()
    palavra_nova=letra
    for i in range(len(palavra)):
        if i!=0:
            palavra_nova += palavra[i]
    return palavra_nova