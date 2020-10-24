with open('macacos-me-mordam.txt', 'r') as file:
    cont = 0
    banana = file.read()
    banana = banana.upper()
    banana = banana.split()
for i in banana:
    if i == 'BANANA':
        cont+=1
print (cont)