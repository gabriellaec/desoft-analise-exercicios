palavras = []
x = 'a'
while x!= 'fim':
    x = input()
    palavras.append(x)
for i in palavras:
    if len(i)<1 or i[0] !='a':
        palavras.remove(i)
for i in palavras:
    print(i)