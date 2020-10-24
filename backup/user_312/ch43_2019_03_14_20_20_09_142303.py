n=1000
dividendo=0
contador=0
maior_arvore=0
maior_numero=0
while n!=0:
    dividendo=n
    while dividendo!=1:
        if dividendo%2==0:
            dividendo=dividendo/2
        else:
            dividendo=dividendo*3+1
        contador=contador+1
    if contador>maior_arvore:
        maior_arvore=contador
        maior_numero=n
    n=n-1
    contador=0
print(maior_numero)