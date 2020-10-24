with open('macacos-me-mordam.txt', 'r') as arquivo:
    cont = arquivo.read()
l = cont.split()
ll = []
for e in l:
    ll.append(e.lower())
s = 'banana'
num = 0
for e in ll:
    if e == s:
        num += 1
print(num)