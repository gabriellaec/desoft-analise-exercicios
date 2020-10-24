valor=int(input("Qual o valor da casa?"))
salário=int(input("Qual o seu salário?"))
anos=int(input("Quantos anos vai pagar?"))
if (valor/(anos*12))<(salário*0.3):
    print ("Empréstimo aprovado") 
else:
    print ("Empréstimo não aprovado")

