b = []
a = float(input('Diga um número: '))
i = 0
while i<len(b) and a!='0':
    b.append(a)
    a = float(input('Diga um número: '))
    i += 1
if a =='0':
    print (sum(b))