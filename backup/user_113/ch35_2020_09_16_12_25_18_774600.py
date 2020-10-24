soma = 0
x= True
while x==True:
    resp = int(input('Digite um número: '))
    if resp != 0:
        soma += resp
        resp = int(input('Digite um número: '))
    else:
        x = False
    