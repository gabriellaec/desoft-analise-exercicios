dep_ini=float(input("Qual o depósito inicial? "))
i=float(input("Taxa de juros da poupança: "))
mês=1
saldo_f=dep_ini
total_j=0
for mês in range(1,25):
    total_j+=i*saldo_f
    saldo_f*=1+i
    
    print("Saldo do mês {0}: {1:.2f}".format(mês,saldo_f))
    print("Total de juros ganhos até o mês {0}: {1:;2f}".format(mês,total_j)
    
    
    
    