depo = float(input("depo :"))
tax = float(input("tax :"))
t = 24

mes = depo * (tax - 1)

tot = 0


while t > 0:
 
    print('{0:.2f}'.format(mes))

    tot += mes

    mes *= tax

    t -= 1

print('{0:.2f}'.format(tot))