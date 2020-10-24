a = []
b = input("Escreva uma palavra:")
while b != "fim":
	a.append(b)
	b = input("Escreva uma palavra:")
i=0
while i < len(a):
	b = a[i]
	if (len(b) > 1) and (b[0] == "a"):
		print((b)*i)
	i+= 1
