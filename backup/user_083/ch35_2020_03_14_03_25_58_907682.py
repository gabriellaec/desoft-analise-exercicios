n=1
soma=0
soma=True
while(soma):
    a=int(input('me diga um numero: '))
    if a!=0:
        print('me diga um numero')
        soma=soma+a
    else:
        soma=False
print('soma: %d'%soma)