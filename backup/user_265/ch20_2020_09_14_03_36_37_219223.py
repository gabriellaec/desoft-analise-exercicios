a = int (input('Distância em km: '))
if a <= 200:
    def um(a):
        y = 0.5 * a
        return y

else: 
    def dois(a):
        y = 200*0.5 + (a-200)*0.45
        return y
    
print (y)
      