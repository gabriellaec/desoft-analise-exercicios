a=int(input("valor deposito inicial?"))
b=int(input("taxa de juros de uma poupanca"))
juros=(b/100)
i=0
total=0
while i < 24:
    custo=a*juros
    c=a+custo
    a=custo
    i+=1
    total+=c
    print("o valor do custo é {:.2f}".format(custo))
print ("o valor total é {:.2f}".format(total))
    
