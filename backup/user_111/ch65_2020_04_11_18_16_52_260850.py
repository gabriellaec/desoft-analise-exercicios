def capitaliza(palavra):
    letra=palavra[0].upper()
    palavra_nova=letra
    for i in palavra:
        if i==0:
            pass
        else:
            palavra_nova+=i
    return palavra_nova