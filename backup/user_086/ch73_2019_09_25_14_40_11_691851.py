def remove_vogais(string):
    letrasminusculas=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    vogaisminusculas=['a','e','i','o','u']
    stringnova=''
    i=0
    while i<len(string):
        if not string[i] in vogaisminusculas:
            stringnova+=string[i]
        i+=1
    return stringnova