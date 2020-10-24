def pos_arroba(string):
    i=0
    for posicao,caractere in enumerate(string):
        if caractere == '@':
            i=posicao
    return i
            
        
        