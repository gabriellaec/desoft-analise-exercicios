def emprestimo(v,s,a):
    if v/(12*a)>0.3*s:
        return "Empréstimo não aprovado"
    else:
        return "Empréstimo aprovado"
    
v=float(input("Valor da casa a comprar: "))
s=float(input("Valor do salário: "))
a=float(input("Quantidade de anos a pagar: "))