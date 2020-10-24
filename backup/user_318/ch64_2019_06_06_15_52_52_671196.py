def pos_arroba(string):
    i=0
    while i<len(string):
        if string[i] == "@":
            return i
        else:
            i+=1
            
            
def nome_usuario(n):
    x=pos_arroba(n)
    return n[:x]

    