soma = False
s=0
while soma:
    n=int(input("Insira um número: "))
    if n==0:
        soma = True
    else:
        s+=n
print(s)
    