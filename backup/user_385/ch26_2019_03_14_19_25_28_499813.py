a = int(input('Horas?'))
b = int(input('dias?'))
c = int(input('minutos?'))
d = int(input('segundos?'))         

def calcular_segundos (a,b,c,d):
    e = b*24*3600+a*3600+c*60 + d
    return e
print(calcular_segundos (a,b,c,d))
    

