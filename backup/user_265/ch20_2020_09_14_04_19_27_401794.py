a = int (input('Distância em km: '))
def preço(a): 
    if a <= 200:
        print ('{0}' .format (0.5 * a))
    else: 
        print ('{0:.2f}' .format(200*0.5 + (a-200)*0.45))
        

      