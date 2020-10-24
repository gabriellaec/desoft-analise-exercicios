def capitaliza(string):
    print(string)
    if string.isupper():
        return string
    else:
        if " " in string:
            w=string.split()
            w.title()
            z=" ".join(w)
    return string.title()