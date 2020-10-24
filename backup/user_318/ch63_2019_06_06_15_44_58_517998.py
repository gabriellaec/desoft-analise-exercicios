def pos_arroba(string):
    i=0
    while i<len(string):
        if i == "@":
            return i
        else:
            i+=1
        