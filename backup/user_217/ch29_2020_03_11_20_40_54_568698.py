deposito=float(input("Deposito: "))
taxa=float(input('Taxa: '))
i=0
while i <=24:
    M=deposito*i*taxa
    print(M)
    i+=1