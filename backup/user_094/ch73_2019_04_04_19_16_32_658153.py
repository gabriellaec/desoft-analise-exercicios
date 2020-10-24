def remove_vogais(string):
    string=list(string)
    i=0
    vogais=['a','e','i','o','u']
    while i<len(string):
        if string[i] in vogais:
            del (string[i])
        else:
            i+=1
   
    string = ''.join(string)
    return string