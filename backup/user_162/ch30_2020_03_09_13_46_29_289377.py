i = 0
inicial = float(input())
mensal = float(input())
juros = float(input())
f = inicial
inicial += mensal

while i < 24:
    inicial += mensal + inicial*(juros)
    print("{:.2f}".format(inicial))
    i+=1
    
print("seu ganho total é {:.2f}".format(inicial - f))
    
