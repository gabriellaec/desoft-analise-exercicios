lista = []
num = int(input("Qual o número inteiro e positivo?"))
i = 0
while num > 0:
    lista.append(num)
    num = int(input("Qual o número inteiro e positivo?"))
    i += 1
    
print(lista[-1::-1])