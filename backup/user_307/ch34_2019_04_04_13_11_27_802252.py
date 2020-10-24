ini=float(input('qual seu depósito inicial? '))
juros=float(input('qual a taxa de juros? '))

i=1

while i<=24:
	y=ini*((1+(juros)/100)**i)
	print (y)
	i+=1
print(('{0:.2f}').format(y-ini))
	