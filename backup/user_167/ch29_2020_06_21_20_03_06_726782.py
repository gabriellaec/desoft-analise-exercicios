a=int(input("valor deposito inicial?"))
b=int(input("taxa de juros de uma poupanca"))
i=0
total=0
while i < 24:
    custo=a*b
    i+=1
    total+=custo
    print("o valor do custo é {:.2f}".format(custo))
print ("o valor total é {:.2f}".format(total))
    
