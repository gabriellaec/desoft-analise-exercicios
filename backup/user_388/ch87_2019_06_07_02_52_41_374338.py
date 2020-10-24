with open('churras.txt', 'r') as f:
    arquivo  = f.readlines()
soma = 0
for i in arquivo:
    x = i.split(',')
    soma += int(x[1])*float(x[2])
    
print(soma)