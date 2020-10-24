dep = float(input("Qual o depósito inicial?"))
tx = float(input("Qual a taxa de juros?"))

i = 1
total = 0

while i < 24:
    total = dep*(1+tx)
    print("R$ {0: .2f}".format(total))
    
print("R$ {0: .2f}".format(total-dep))