def capitaliza(string):
    if not string.isupper():
        return string.title()
    else:
        r=string.lower()
        return r.title()