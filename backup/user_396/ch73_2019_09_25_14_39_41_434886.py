def remove_vogais(x):
    y = ""
    i = 0
    while i < len(x):
        if x[i] != "a" or x[i] != "e" or x[i] != "i" or x[i] != "o" or x[i] != "u":
            y += x[i]
            return y
        i += 1