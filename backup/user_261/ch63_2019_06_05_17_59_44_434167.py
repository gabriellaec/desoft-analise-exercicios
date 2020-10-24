def pos_arroba(email):
    pos=0
    for e in email:
        if e=="@":
          pos=email[e]
    return pos