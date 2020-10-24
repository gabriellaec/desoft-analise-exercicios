a=int(input("Qual seu deposito inicial? "))
e=a
b=int(input("Qual sua taxa de juros? "))
d=0
c=1
while c<24:
    c=c+1
    a=a+(a*(b/100))
    d=d+a
    print (a)
    
print (d-e)