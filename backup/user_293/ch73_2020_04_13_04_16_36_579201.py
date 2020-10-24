def remove_vogais(string):
    a = ""
    for e in string:
        if e == "a" or e == "e" or e == "i" or e == "o" or e == "u":
            e = ""
        a = a + e
    return a
