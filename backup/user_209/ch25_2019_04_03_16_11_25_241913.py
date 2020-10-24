x = float(input("Quantos km você vai percorrer?: "))
if x <= 200:
    y = 0,5*x
elif x > 200:
    y = 100 + 0,45 *(x - 200)
return y
print ('(0:.2f)'.format(y))
    
      