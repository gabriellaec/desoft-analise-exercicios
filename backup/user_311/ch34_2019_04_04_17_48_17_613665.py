x = float(input("depósito inicial:"))
y = int(input("taxa de juros:"))
i = 0
montante = 0          
          
while i <= 24:
          montante = x*(1+(y/100))**i
          print ('{0:.2f}'.format(montante))
          i += 1

print('{0:.2f}'.format(montante - x*(1+(y/100))**1))
