soma=[0]
zero=False
x=input("digite um numero")
soma.append(int(x))
if x!= "0":
    zero=True
while zero==True:
    x=input("digite um numero")
    soma.append(int(x))
    if x=="0":
        zero=False
    else:
        zero=True
print(sum(soma))