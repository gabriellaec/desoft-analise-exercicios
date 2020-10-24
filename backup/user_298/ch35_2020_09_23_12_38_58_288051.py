fazendo_conta = True
soma = 0 
while fazendo_conta:
    a = int(input("Fale um numero(0 para parar): "))
    soma += a   
    if a == 0:
        fazendo_conta = False
print(soma)