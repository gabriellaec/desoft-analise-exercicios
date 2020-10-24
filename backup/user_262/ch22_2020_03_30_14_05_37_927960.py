pd=int(input("qnts por dia?"))
ano=int(input("qntsanos?"))
def dias_perdidos(pd,ano):
    t=(pd*365*ano*10)/24*60
    print(t)