def calcula_valor_devido(t):
    F =  C * (( 1 + i ))**t
    return F
C = int(input("Quantidade de capital emprestado? "))
i = int(input("Quantiade de juros? "))
t = int(input("Quantidade de meses devendo?"))
print(calcula_valor_devido) 
