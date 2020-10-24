numposi = []
num = int(input("Entre com um numero inteiro: "))
while num > 0:
    numposi.append(num)
    num = int(input("Entre com um numero inteiro: "))
i = -1
size = len(numposi)
size = size-1
while size>i:
    print(numposi[size])
    size -= 1
   