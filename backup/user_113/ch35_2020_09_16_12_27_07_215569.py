soma = 0
x= True
while x==True:
    resp = int(input('Digite um número: '))
    if resp != 0:
        soma += resp
    else:
        x = False
print(soma)