valor = int(input("Valor da casa a comprar: ")) 
salario = int(input("Salário: ")
anos = (input("Anos a pagar: ")
prestacao = valor / anos * 12
if prestacao < 0.3 * salario:
    print ("Emprestimo aprovado")
else: 
    print ("Emprestimo nao aprovado")