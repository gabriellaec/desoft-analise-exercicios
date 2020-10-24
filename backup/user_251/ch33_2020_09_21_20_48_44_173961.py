def eh_primo(a):
    divisor = 2
    if a == 1 or a == 0:
        return False
    
    if a == 2:
        return True
    
    while a % divisor != 0 and divisor < (a-1):
        divisor += 1
    if a % divisor == 0:
        return False
    
    else:
        return True
numero_de_primos = 0
contador = 0
b = int(input("digite o número menor: "))
c = int(input("digite o número maior: "))
while contador < b:
    contador += 1
while b <= contador and contador <c:
    if eh_primo(contador):
        numero_de_primos += 1
        contador += 1
    else:
        contador += 1

print(numero_de_primos)

