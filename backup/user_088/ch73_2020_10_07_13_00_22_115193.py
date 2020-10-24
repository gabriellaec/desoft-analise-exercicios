def remove_vogais(string):
    palavra=''
    vogais=["a","e","i","o","u"]
    i=0
    while(i<len(string)):
        if(string[i] not in vogais):
            palavra+=string[i]
        i+=1
    return palavra