def remove_vogais(word):
    nova=''
    x=0
    while x<len(word):
        if word[x]!='a' and word[x]!='e' and word[x]!='i' and word[x]!='o' and word[x]!='u':
            nova.join(word[x])
        x+=1
    return nova