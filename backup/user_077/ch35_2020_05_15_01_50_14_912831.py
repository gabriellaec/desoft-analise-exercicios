perguntar=True
soma=0
while perguntar:
    a=int(input('insira um número'))
    soma+=a
    if a==0:
        print(soma)
        perguntar=False
    else:
        perguntar=True
    