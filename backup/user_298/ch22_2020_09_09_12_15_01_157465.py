a= input("Quantos cigarros voce fuma por dia? ")
b= input("Ha quantos anos? ")
a= int(a)
b= int(b)
def vida(a,b):
    fumado= a*b*365
    perdido= (fumado)/144
    return perdido
print(vida(a,b))