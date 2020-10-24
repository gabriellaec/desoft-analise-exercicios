a=int(input("valor deposito inicial?"))
b=int(input("taxa de juros de uma poupanca"))
i=0
total=0
while i < 24:
    custo=a*b
    total+=custo
    print(custo.format(%.2f))
    print(total.format(%.2f))
    
