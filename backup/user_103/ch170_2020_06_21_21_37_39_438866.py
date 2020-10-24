def capitaliza(word):
    letra=word[0].upper()
    palavra_nova=letra
    for i in range(1,len(word)):
        palavra_nova+=word[i]
    return palavra_nova

def apaga_repetidos(palavra):
    palavra_certa = capitaliza(palavra)
    palavra_final=[]
    for i in range(len(palavra_certa)):
        if palavra_certa[i] not in palavra_final :
            palavra_final.append(palavra_certa[i])
        else:
            palavra_final.append(*)
    return ''.join(palavra_final)

