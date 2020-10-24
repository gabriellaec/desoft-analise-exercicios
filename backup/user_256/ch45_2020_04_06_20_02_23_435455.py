dig = int(input("Digite numeros positivos: "))
vazia = []

while dig > 0:
    vazia.append(dig)
    dig = int(input("Digite numeros positivos: "))

i= len(vazia)-1
while i >= 0:
    print(vazia[i])
    i-=1
    
    
    