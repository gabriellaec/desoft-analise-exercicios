def remove_vogais(string):
    i=0
    string=list(string)
    while i<len(string)-1:
        if string[i]=="a" or string[i]=="u" or string[i]=="o" or string[i]=="e" or string[i]=="i":
            del(string[i])
        i+=1
    return string