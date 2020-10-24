def capitaliza(string):
    print(string)
    if string.isupper():
        return string
    else:
        if " " in string:
            w=string.split()
            for e in w:
                e.title()
            z=" ".join(w)
    return string.title()