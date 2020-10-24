valor = int(input("Quanto custa a casa?"))
salário = int(input("Qual seu salário?"))
anos = int(input("Em quantos anos vai pagar?"))
meses = anos * 12
if valor/meses > 0.3 * salário:
    print ("Empréstimo não aprovado")
else:
    print ("Empréstimo aprovado")