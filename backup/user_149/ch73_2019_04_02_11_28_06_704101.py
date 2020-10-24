def remove_vogais(string):
    x=0
    nova=''
    while x<len(string):
        if string[x]!='a' and string[x]!='e' and string[x]!='i' and string[x]!='u' and string[x]!='o':
            nova+=string[x]
        x+=1
    return(nova)