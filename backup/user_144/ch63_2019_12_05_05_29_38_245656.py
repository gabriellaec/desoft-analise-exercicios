
def pos_arroba1(email):
    pos = -1
    for i in range(len(email)):
        if email[i] == '@':
            pos = i
            
    return pos