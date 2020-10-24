def funcao(string):

    i=0

    while i < len(string):
        if string[i]=='@':
            return string[:i]
        i+=1