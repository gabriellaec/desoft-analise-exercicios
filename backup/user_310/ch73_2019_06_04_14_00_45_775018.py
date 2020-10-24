def remove_vogais(s):
    for i in "AEIOU":
        s = s.replace(i, "")
    return s
