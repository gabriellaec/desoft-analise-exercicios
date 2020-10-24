num=int(input('Digite seu número para adicionar: '))
while num!=0:
    numero=int(input('Digite seu número para adicionar ou 0 para somar: '))
    if numero==0:
        break
    else:
        num+=numero
print(num)