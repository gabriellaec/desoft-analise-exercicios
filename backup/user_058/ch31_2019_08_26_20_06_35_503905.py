def emprestimo(x,y,z):
    if x/z<=(y*0.3):
        return "Empréstimo aprovado"
    else:
        return "Empréstimo não aprovado"





x=(float(input("Qual o valor da casa que deseja comprar? ")))
y=(float(input("Qual seu salário mensal? ")))
z=(float(input("Em quantos anos pretende pagar? ")))
