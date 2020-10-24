def pos_arroba(email):
    i = 0
    while i < len(email):
        if email[i] == "@":
            posicao = i+1
            break
        else:
            i += 1
    return posicao
        
print(pos_arroba(luccapbs@hotmail.com))
       