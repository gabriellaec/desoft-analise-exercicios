running = True
lista_num = []

while running:
    num = int(input('Digite um numero: '))
    if num > 0:
        lista_num.append(num)
    elif num <= 0:
        running = False
        
        
i = len(lista_num)
while i > 0:
    print(lista_num[i - 1])
    i-=1
              