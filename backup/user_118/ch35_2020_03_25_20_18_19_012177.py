b = []
a = int(input('Diga um número: '))
c = sum(b)
i = 0
while i<len(b) and a!='0':
    b.append(a)
    a = int(input('Diga um número: '))
    i += 1
if a=='0':
    print (c)
