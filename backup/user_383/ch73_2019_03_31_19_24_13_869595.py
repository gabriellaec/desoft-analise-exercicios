def remove_vogais(palavra):
    cont=0
    while cont<len(palavra):
        if palavra[cont]=='a' and palavra=='e' and palavra=='i' and palavra=='o' and palavra=='u':
            del palavra[cont]
    return palavra
            