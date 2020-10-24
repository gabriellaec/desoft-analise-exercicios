km = float(input("quantos km senhor?"))    
if km <= 200:
         preco = km*0.50
         print(float(preco.round(2)))
else:
         preco = (km-200)*0.45 + 200*0.50
         print(float(preco.round(2)))