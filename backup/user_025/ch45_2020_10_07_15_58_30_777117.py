numposi = []
numeros = int(input('Digite número inteiro: '))
while numeros > 0:
    numposi.append(numeros)
    numeros = int(input('Digite número inteiro: '))
    
i = -1
size = len(numposi)
size = size - 1

while size>1:
    print(numposi[size])
    size -= 1