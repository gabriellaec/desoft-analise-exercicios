def remove_vogais(x):
    y = ""
    i = 0
    while i < len(x):
        if x[i] != "a" and x[i] != "e" and x[i] != "i" and x[i] != "o" and x[i] != "u":
            y += x[i]
        i += 1
        return y