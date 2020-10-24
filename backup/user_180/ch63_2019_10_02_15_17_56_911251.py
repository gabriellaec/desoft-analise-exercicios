def pos_arroba(string):
    cont = 0
    for i in string:
        if i == "@":
            return string[cont]
    cont+=1