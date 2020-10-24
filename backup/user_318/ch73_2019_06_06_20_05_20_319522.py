def remove_vogais(s):
    a=[]
    a=list(s)
    for i in a:
        if i == "a" or i == "e" or i == "o" or i == "i" or i == "u":
            del(a[i])
    b = "".join(a)
    return b
