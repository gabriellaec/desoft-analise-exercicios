soma=0
n=int(input("Digite um número (0 para somar o total): "))
soma+=n
while n!=0:
    n=int(input("Digite um número (0 para somar o total): "))
    soma+=n
    if n==0:
        print(soma)