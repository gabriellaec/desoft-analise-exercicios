def lista_sufixos(a):
    lista = []
    srt = ''
    for i in range(len(a)):
        if a[i] == '-':
            for x in a[a[i]:]:
                if x != ' ':
                    srt += x
                else:
                    break
            lista.append(srt)
            srt = ''
    return lista