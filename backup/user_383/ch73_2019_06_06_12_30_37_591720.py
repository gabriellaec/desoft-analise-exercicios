def remove_vogais(palavra):
    cont=0
    palavra = palavra.lower()
    while cont<len(palavra):
        if palavra[cont]=='a' or palavra=='e' or palavra=='i' or palavra=='o' or palavra=='u':
            palavra.replace('a','')
            palavra.replace('e','')
            palavra.replace('i','')
            palavra.replace('o','')
            palavra.replace('u','')
        cont+=1
    return palavra
            