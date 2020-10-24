from random import randint
dado1=(randint(1,10))
dado2=(randint(1,10)) 
dados=dado1+dado2
dinheiro=10

#fase de dicas:

a=int(input('Escolha um número: '))
b=int(input('Escolha um número maior ou igual ao anterior fornecido: '))
P=True
while P: 
    if (dados < a) :
        print("Soma menor")
    elif (dados > b) :
        print("Soma maior")
    else : 
        P=False
print("Soma no meio")

#Fase de chutes:

print(dinheiro 'dinheiros disponível')
c=int(input('Quantos chutes você quer comprar(cada chute custa 1 dinheiro)?: '))
    
    
    