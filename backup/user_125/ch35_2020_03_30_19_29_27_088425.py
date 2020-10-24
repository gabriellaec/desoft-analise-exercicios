a=int(input('me de um número '))
soma=True
contador=a
while soma and a!=0:
    a=int(input('me de um número'))
    contador+=a
    if a==0:
        soma=False
print(contador)