def remove_vogais(x):
    for i in x:
        if i == "a" or "e" or "i"or"o"or"u":
            x.replace(i,"")
    return(x)
