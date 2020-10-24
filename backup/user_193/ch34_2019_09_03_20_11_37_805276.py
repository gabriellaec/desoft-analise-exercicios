a=int(input("Qual seu deposito inicial? "))
b=int(input("Qual sua taxa de juros? "))

c=1
while c<24:
    c=c+1
    a=a+(a*(b/100))
    print (a)