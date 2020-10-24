v=input("valor emprestado?")
i=input("taxa de juros?")
n=input("prazo?")

def calcula_valor_devido(v,i,n):
    p=int(v)*(1+int(i))**int(n)
    return p

print(calcula_valor_devido(v,i,n))