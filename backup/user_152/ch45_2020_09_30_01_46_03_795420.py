numposi = []
num = int(input("Entre com um numero inteiro: "))
while num > 0:
    numposi.append(num)
    num = int(input("Entre com um numero inteiro: "))
i = -1
size = len(numposi)
while size>i:
    print(numposi[size-1])
    size -= 1
   