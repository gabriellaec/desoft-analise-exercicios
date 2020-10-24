a=float(input("deposito:")
b=float(input("taxa de juros:")
mes=1
while mes<24:
   y=a*(1+b)**mes
   print(y:.2f)
   mes+=1   
        
c= a*(1+b)**24
print(c:.2f)