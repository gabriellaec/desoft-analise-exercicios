with open('churras.txt','r') as ch:
    soma = 0
    for line in ch:
        a = line.split(",")
        x = float(a[1])
        y = float(a[2])
        prod = x * y
        soma += prod

print(soma)