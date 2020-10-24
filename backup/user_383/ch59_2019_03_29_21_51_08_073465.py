def conta_a(palavra):
    cont=0
    contador=0
    while cont<len(palavra):
        if palavra[cont]=='a':
            contador+=1
    	cont+=1
    return contador
palavra=input('digite a palavra')
print(conta_a(palavra))
