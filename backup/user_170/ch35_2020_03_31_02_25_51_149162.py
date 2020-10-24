acabou = False
somatoria =[]
while acabou == False:
    n = float(input('Entre com um numero: '))
    if n != 0:
        somatoria.append(n)
    else:
        acabou = True
print(sum(somatoria))