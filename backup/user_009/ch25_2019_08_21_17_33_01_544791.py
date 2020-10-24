km = float(input('km: '))
if km <= 200:
	print(0.5 * km)
else:
	print((200 * km) + ((km - 200)*0.45)