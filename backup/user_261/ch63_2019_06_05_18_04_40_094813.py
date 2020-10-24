def pos_arroba(email):
    i=0
    pos=0
    while i <len(email):
        if email[i]=="@":
          pos=i
    return pos