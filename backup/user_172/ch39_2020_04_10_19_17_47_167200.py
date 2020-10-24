y = True
i = 0
x<1000
while y:
    if x%2 == 0:
        x = x/2
        i+=1
    elif x%2 != 0:
        x = 3*x + 1
        i+=1
    elif x == 1:
        y = False
        
print (x)

      
    