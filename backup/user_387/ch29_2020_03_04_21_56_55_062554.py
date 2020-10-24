depo = float(input("depo :"))
tax = float(input("tax :"))
t = 23

mes = depo * tax

tot = 0

print(depo)

while t > 0:
 
    print('{0:.2f}'.format(mes + 1000))

    tot += mes

    mes *= (tax + 1)

    t -= 1

print('{0:.2f}'.format(tot + 1000))