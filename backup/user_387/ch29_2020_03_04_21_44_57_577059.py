depo = float(input("depo :"))
tax = float(input("tax :"))
t = 24

mes = depo * tax

tot = 0


while t > 0:
 
    print(truncate(mes,2))

    tot += mes

    mes *= (tax + 1) 

    t -= 1

print(truncate(tot,2))