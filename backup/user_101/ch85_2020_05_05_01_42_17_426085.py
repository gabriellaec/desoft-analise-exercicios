with open('macacos-me-mordam.txt', 'r') as arquivo:
    cont = arquivo.read()
str = 'banana'
num = 0
i = 0
while i < len(cont):
    l = e.lower()
    i += 1
    if l == str:
        num += 1

print(num)