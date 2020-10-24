palavras = []
x = input()
while x!= 'fim':
    palavras.append(x)
    x = input()
for i in palavras:
    if len(i)>0 and i[0] == 'a':
        print(i)