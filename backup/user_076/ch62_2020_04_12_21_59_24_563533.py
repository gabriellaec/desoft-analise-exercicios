def pos_arroba (email):
    i = 0 
    while i<len(str(email)):
        x = email[i]
        if x == "@":
            posição = i
        i+=1
    return posição