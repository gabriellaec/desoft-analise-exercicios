val = float(input("Qual o valor do imovel? "))
sal = float(input("Qual o seu salario? "))
anos = float(input("Quantos anos vai pagar? "))
meses = anos*12
prestacao = val/meses
if prestacao <= 0.30*sal:
    print("Empréstimo aprovado")
else:
    print("Empréstimo não aprovado")