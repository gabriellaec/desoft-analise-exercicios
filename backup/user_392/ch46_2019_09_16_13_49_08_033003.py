x = True
lis = []
i = 0

while x:
    z = input('digite palavras, e fim para parar: ')
    lis.append(z)
    if z == 'fim':
        x = False
while i < len(lis):
    palavra = lis[i]
    if palavra[0] == 'a':
        print(lis[i])
    i+=1


    