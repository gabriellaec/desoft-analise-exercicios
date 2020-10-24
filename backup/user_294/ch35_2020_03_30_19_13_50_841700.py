num=0
i=True
soma=0
while i:
    soma+=num
    num=int(input('digite um numero: '))
    if num==0:
        print(soma)
        i=False