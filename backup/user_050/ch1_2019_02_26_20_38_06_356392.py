def Calcula_Valor_Devido(n1,n2,n3):
    V = n1*(1+n2/100)**n3
    return V;

c = int (input("digite o valor emprestado: "))
i = int (input("digite a taxa de juros ao mês: "))
t = int (input("digite o número de meses que se passaram desde o empréstimo: "))
V = Calcula_Valor_Devido(c,i,t)

print(V)