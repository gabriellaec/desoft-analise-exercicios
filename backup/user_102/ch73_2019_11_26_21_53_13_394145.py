def remove_vogais(x):
    for i in x:
        if i == "a" or "e" or "i"or"o"or"u":
            i.replace(i,"")
   	return x
