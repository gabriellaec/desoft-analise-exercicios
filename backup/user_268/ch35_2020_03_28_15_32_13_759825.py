soma=False
p=0
l=0
while not soma:
    p = float(input("numero: "))
    l+=p
    if p == 0:
        soma= True
print(l)