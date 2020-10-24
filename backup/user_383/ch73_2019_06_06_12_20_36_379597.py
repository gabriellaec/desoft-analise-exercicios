def remove_vogais(palavra):
    cont=0
    while cont<len(palavra):
        if palavra[cont]=='a' or palavra=='e' or palavra=='i' or palavra=='o' or palavra=='u':
            del palavra[cont]
        cont+=1
    return palavra
            