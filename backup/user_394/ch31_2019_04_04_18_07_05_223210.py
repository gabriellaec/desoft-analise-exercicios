valor = input("Quanto custa a casa?")
salário = input("Qual seu salário?")
anos = input("Em quantos anos vai pagar?")
meses = anos * 12
if valor/meses > 0.3 * salário:
    print ("Empréstimo não aprovado")
else:
    print ("Empréstimo aprovado")