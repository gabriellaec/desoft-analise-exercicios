with open('churras.txt', 'r') as f:
    arquivo  = f.readlines()
soma = 0
for i in arquivo:
    x = i.split(',')
    soma += x[1]*x[2]
    
print(soma)