def tamanho(x):
    contador = 1
    while 1 < x < 1000:
        if x % 2 == 0:
            x = x/2
        else:
            x = 3*x + 1
        contador += 1
    return contador
nms = 1
ms = 1
x = 2

while 2 <= x < 1000:
    if tamanho(x) > ms:
        ms = tamanho(x)
        nms = x
        x = x + 1
print(nms)