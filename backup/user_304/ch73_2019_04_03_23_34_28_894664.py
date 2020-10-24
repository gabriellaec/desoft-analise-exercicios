def remove_vogais (PALAVRA):
    s=''
    i=0
    while i<len(PALAVRA):
        if PALAVRA[i]!='A' and PALAVRA[i]!='E' and PALAVRA[i]!='I' and PALAVRA[i]!='O' and PALAVRA[i]!='U':
            s+=PALAVRA[i]
        i+=1
    return s
            