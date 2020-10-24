def pos_arroba(email):
    pos = 0
    while email[pos] != "@":
        pos += 1
    if email[pos] == "@":
        return pos
   