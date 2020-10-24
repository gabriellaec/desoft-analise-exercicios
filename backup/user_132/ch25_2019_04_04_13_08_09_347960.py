d = int(input("qual a distancia percorrida? "))

valor = 0

if d <= 200:
    valor = d * 0.5
else:
    valor = 100 + (200 - d)*0.45
    
print(ronf(valor,2))