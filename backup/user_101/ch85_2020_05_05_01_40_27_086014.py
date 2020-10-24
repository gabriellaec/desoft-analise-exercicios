with open('macacos-me-mordam.txt', 'r') as arquivo:
    cont = arquivo.read()
str = 'banana'
num = 0
for e in cont:
    l = e.lower()
    if l == str:
        num += 1

print(num)