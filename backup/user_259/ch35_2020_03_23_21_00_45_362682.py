soma = True
s=0
while soma:
    n=int(input("Insira um número: "))
    if n==0:
        soma = False
    else:
        s+=n
print(s)
    