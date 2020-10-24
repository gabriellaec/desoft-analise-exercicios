def remove_vogais(s):
    for i in "aeiou":
        s = s.replace(i, "")
    return s
