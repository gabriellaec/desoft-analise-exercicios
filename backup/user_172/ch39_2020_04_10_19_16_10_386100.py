y = True
while y:
    if x%2 == 0:
        x = x/2
    elif x%2 != 0:
        x = 3*x + 1
    elif x == 1:
        y = False
        
print (x)

      
    