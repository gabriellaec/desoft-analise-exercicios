km = int(input('km: '))
if km <= 200:
    print('{0:.2f}'.format(km/2))
else:
	print('{0:.2f}'.format((200 * km) + ((km - 200)*0.45)))