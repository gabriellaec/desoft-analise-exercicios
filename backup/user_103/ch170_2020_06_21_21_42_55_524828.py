def apaga_repetidos(palavra_certa):
    palavra_final=[]
    for i in range(len(palavra_certa)):
        if palavra_certa[i] not in palavra_final :
            palavra_final.append(palavra_certa[i])
        else:
            palavra_final.append('*')
    return ''.join(palavra_final)

