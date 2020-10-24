i = 0
di = float(input("Qual o valor do seu deposito? "))
tj = float(input("Qual a taxa de juoros? "))

while i < 24:
    di += di*(tj/100)
    print(di)
    i+=1
    
print("seu ganho total é {:.2f}".format(di))
    