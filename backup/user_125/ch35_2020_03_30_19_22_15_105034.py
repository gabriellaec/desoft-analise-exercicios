a=int(input('me de um número '))
soma=True
contador=0
while a!=0:
    a=int(input('me de um número'))
    contador+=a
    if a==0:
        print(contador)
        soma=False