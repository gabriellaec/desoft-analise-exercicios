n=float(input("digite um numero:"))
s=0
i=0
while n!=0:
    s+=n
    n=float(input("digite outro numero:"))   

    i+=1
print('A soma desses numeros é: {0}'.format(s))