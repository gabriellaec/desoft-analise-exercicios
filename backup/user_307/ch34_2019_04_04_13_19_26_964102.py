ini=float(input('qual seu depósito inicial? '))
juros=float(input('qual a taxa de juros? '))

i=1

while i<=24:
	M=ini*((1+juros)**i)
	print (M)
	i+=1
print(('{0:.2f}').format(M-ini))
	