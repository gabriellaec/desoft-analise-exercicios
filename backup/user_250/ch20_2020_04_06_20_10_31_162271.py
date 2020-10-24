x = float(input("Qual a distância a ser viajada?: "))
if x > 200:
    q = x-200
    p = format(100+(0.45*q), '.2f')
    return(p)
else:
    p = format((x*0.5), '.2f')
    return(p)