def pos_arroba(n):
    posicao=0
    i=0
    while i<len(n):
        if n[i]!='@':
            posicao+=1
        else:
            break
        i+=1
    return posicao
    
print(pos_arroba("inspe@"))