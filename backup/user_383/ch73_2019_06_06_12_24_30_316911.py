def remove_vogais(palavra):
    cont=0
    palavra = palavra.lower()
    while cont<len(palavra):
        if palavra[cont]=='a' or palavra=='e' or palavra=='i' or palavra=='o' or palavra=='u':
            palavra[cont].remove()
        cont+=1
    return palavra
            