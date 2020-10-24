a= input("Quantos cigarros voce fuma por dia? ")
b= input("Ha quantos anos? ")
a= float(a)
b= float(b)
b= b*365
def vida(a,b):
    por_dia= (a*10)/1440
    td= por_dia*b
    return td