with open('macacos-me-mordam.txt', 'r') as file:
    x = file.read()
y=x.lower()
z=y.count('banana')
print(z)