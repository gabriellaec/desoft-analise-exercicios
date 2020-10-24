dist=float(input('Qual distância desejada?'))
if dist<=200:
	y=dist*0.5
else:
	y=100+(dist*0.45)
print(("a distância desejada é {0:.2f}").format(y))