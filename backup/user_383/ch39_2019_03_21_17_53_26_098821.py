numeros=int(input('Digite os números :'))
soma=0
while numeros != 0:
    soma += numeros
    numeros = int(input('Digite os números :'))

    if numeros==0:
        print(soma)