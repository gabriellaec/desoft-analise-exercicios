dep = float(input("Qual o depósito inicial?"))
tx = float(input("Qual a taxa de juros?"))

i = 0
total = 0
mes=[0]*24

while i < 24:
    total = dep*(1+tx)
    mes[i] = dep*(1+tx)
    i=i+1
    
print("R$ {0: .2f}".format(total-dep))
print("R$ {0: .2f}".format(mes))