def capitaliza(string):
    caps=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    naocaps=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    i=0
    if string[0] in naocaps:
        while string[0]!=naocaps[i]:
            i+=1
    if string[0] in caps:
        return string
    else:
        return 'Erro'
    listanova=''
    listanova+=caps[i]
    n=1
    while n<len(string):
        listanova+=string[n]
        n+=1
    return listanova