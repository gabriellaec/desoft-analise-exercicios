i = 0
inicial = float(input())
mensal = float(input())
juros = float(input())/100
f = inicial
inicial += mensal

while 0 < i < 24:
    
    inicial += mensal + inicial*(juros)
    print(inicial)
    i+=1
    
print("seu ganho total é {:.2f}".format(inicial - f))
    
