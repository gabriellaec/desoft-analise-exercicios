lista_nums = []

a = 5
soma = 0

while a != 0:

    a = float(input("Numero :"))
    lista_nums.insert(0, a) 


for num in lista_nums:
    soma = soma + num

print(soma)
