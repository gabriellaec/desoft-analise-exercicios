numero = float(input("digite um numero / 0 para parar :"))

while numero != "0":
    soma = numero + numero
    numero = float(input("digite um numero / 0 para parar :"))
    if numero == "0":
        print(soma)
    