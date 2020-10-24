d = int(input("qual a distancia percorrida? "))

valor = 0

if d < 200:
    valor = d * 0.5
else:
    valor = 100 + (d - 200)*0.45
    
print(round(valor,2))