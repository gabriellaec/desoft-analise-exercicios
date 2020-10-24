i = 0
di = float(input("Qual o valor do seu deposito? "))
tj = float(input("Qual a taxa de juoros? "))
f = di

while i < 24:
    di += di*(tj)
    print("{:.df}".format(di))
    i+=1
    
print("{:.2f}".format(di - f))