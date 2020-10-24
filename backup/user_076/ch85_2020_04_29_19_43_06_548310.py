with open('macacos-me-mordam.txt','r') as arquivo:
    conteúdo = arquivo.read()
    i=0
    número_de_bananas = 0
    while i+5 < len(conteúdo):
        if conteúdo[i] == 'b' or conteúdo[i] == 'B':
            if conteúdo[i+1] == 'a' or conteúdo[i+1] == 'A':
                if conteúdo[i+2] == 'n' or conteúdo[i+2] == 'N':
                    if conteúdo[i+3] == 'a' or conteúdo[i+3] == 'A':
                        if conteúdo[i+4] == 'n' or conteúdo[i+4] == 'N':
                            if conteúdo[i+5] == 'a' or conteúdo[i+5] == 'A':
                                número_de_bananas+=1
        i+=1
        
print(número_de_bananas)
                                
                            