contador=1
x=1
while contador<100:
    soma = x+(1/(2**contador))
    contador+=1
    x=soma+x
print(x)