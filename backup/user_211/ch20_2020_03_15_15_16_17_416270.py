x=float(input("qual a distância em Km?"))
if x<=200:
    y=x*.5
elif x>200:
    y=100+(x-200)*0.45
	
print("{0:.2f}" .format(y))
