def capitaliza(palavra):
    letra=palavra[0].upper()
    palavra_nova=letra
    for i in range(1,len(palavra)):
        palavra_nova += palavra[i]
    return palavra_nova