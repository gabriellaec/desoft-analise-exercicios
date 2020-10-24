def remove_vogais(palavra):
    i=0
    while i<len(palavra):
        if palavra[i]=='a' or palavra[i]=='e' or palavra[i]=='i' or palavra[i]=='o' or palavra[i]=='u':
            palavra=palavra.replace(palavra[i],'')
        i+=1
    return palavra