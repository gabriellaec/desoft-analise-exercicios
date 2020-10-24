with open('macacos-me-mordam.txt','r') as arquivo:
    conteudo = arquivo.read()
    conteudo.strip(',')
    conteudo.strip(' ')
    ocorrencias = 0
    i = 0
    c = 0
    while i<len(conteudo):
        if len(conteudo[i])==6:
            if conteudo[i][0]=='B' or conteudo[i][c]=='b':
                if conteudo[i][1]=='A' or conteudo[i][c]=='a':
                    if conteudo[i][2]=='N' or conteudo[i][c]=='n':
                        if conteudo[i][3]=='A' or conteudo[i][c]=='a':
                            if conteudo[i][4]=='N' or conteudo[i][c]=='n':
                                if conteudo[i][5]=='A' or conteudo[i][c]=='a':
                                    ocorrencias+=1
        i+=1
        