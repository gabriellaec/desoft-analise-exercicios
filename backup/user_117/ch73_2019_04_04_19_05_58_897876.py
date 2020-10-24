def remove_vogais(string):
    i=0
    string=list(string)
    v=['a','e','i','o','u']
    while i<len(string):
        if string[i] in v:
            del string[i]
        else:
            i+=1
    string= ''.join(string)
    return string