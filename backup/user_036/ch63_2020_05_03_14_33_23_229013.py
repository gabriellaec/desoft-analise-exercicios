def pos_arroba(string):
    i = 0
    pos = -1
    while i < len(string):
        if string[i] == '@':
            pos = i
        i+=1
    return pos

def usuario(email):
    pos = pos_arroba(email)
    return(email[0:pos])