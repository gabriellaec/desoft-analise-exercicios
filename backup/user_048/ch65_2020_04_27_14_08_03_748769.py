def capitaliza(string):
    print(string)
    if string.isupper():
        return string
    else:
        if " " in string:
            w=string.split()
            lista=[]
            for e in w:
                M=e.title()
                lista.append(M)
            return " ".join(lista)
        else:
            b=string.title()
            return b