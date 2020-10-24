depo = float(input("depo :"))
tax = float(input("tax :"))
t = 24

mes = depo * (1 - tax)

tot = 0

while t > 0:
    
    print('{0:.2f}'.format(depo))
    
    depo*= tax

    tot += mes

    mes *= tax

    t -= 1

print('{0:.2f}'.format(tot))