caixa_inicial= float(input("Qual o seu caixa incial? "))
juros=float(input("Qual a taxa de júros aplicada? "))
a=caixa_inicial+caixa_inicial*juros**1
a1=a+a*juros**1
t=0
while t<=24:
    total=caixa_incial+caixa_inicial**t
    print(total)
    t+=1