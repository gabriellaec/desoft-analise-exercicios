d=int(input('distancia? '))
if d<=200:
	f=d*0.5
else:
	f=100+(d-200)*0.45
print (f)