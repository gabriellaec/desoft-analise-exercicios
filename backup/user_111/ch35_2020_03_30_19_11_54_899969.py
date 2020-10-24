num=0
i=True
soma=0
while i:
    soma+=num
    num=int(input("Digite um número: "))
    if num==0:
        print(soma)
        i=False