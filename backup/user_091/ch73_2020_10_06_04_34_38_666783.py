def remove_vogais(string):
    define='aeiou'
    new=[x for x in string if x not in define]
    i=0
    soma=''
    while i<len(new):
        soma+=new[i]
        i+=1
    return soma
        

    