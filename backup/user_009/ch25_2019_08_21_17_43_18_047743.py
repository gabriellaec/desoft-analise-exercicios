km = int(input('km: '))
if km <= 200:
	b = (0.5 * km)
    print('{:.2f}'.format(b))
else:
	a = ((200 * km) + ((km - 200)*0.45)
    print('{:.2f}'.format(a))