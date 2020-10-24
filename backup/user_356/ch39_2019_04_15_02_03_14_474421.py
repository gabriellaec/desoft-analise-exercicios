n=int(input("Digite um número (0 para somar o total): "))
soma=0
while n!=0:
    soma+=n
    n=int(input("Digite um número (0 para somar o total): "))
    if n==0:
        print(soma)