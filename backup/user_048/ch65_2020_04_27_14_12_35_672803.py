def capitaliza(string):
    print(string)
    if string.isupper():
        return string
    else:
        if " " in string:
            w=string.split()
            w[0]=w[0].title()

            return " ".join(w)
        else:
            b=string.title()
            return b