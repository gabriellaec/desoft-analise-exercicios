def f(x):
    y = (1/2)**x
    return y

indices = range(0, 100)
soma = 0
for n in indices:
    soma += f(n)
    
print(soma)