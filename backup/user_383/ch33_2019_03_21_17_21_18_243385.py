contador = 0
soma_cem=(1/(2**contador))+(1/(2**(contador+1)))

while contador<=99:
    print(soma_cem)
    contador+=1
    soma_cem += contador
