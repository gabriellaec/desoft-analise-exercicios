x = float(input("Quantos km você vai percorrer?: "))
if x <= 200:
    y = 0,5*x
else:
    y = 100 + 0,45 *(x - 200)
print ('(0:.2f)'.format(y))
    
      