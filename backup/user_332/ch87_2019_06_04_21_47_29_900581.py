with open('churras.txt','r') as ch:
    soma = 0
    for line in ch:
        a = line.split(",")
        x = int(a[1])
        y = int(a[2])
        prod = x * y
        soma += prod

print(soma)