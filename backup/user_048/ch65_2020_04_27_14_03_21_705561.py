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
            z=" ".join(lista)
    return z
