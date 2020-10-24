dist = int(input('Qual a distância a ser percorrida em km?')
if dist <= 200:
	p = dist*0.50
else:
	p = 200*0.50 + (dist-200)*0.45
print(p:.02f)