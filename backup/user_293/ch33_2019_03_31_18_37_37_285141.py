contador=1
soma=1
while contador<100:
    x = soma+(1/(2**contador))
    contador+=1
    soma+=x
print(soma)
   