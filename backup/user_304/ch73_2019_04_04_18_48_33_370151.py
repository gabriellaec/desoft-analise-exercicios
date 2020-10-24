def remove_vogais (palavra):
    s=''
    i=0
    while i<len(palavra):
        if palavra[i]!='a' and palavra[i]!='e' and palavra[i]!='i' and palavra[i]!='o' and palavra[i]!='u':
            s+=palavra[i]
        i+=1
    return s
            