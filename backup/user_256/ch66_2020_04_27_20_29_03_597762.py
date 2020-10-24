def lista_sufixos(palavra):
    i=0
    nossa = []
    while i<len(palavra):
        nossa+=palavra[i:].split(',')
        i+=1
    return nossa