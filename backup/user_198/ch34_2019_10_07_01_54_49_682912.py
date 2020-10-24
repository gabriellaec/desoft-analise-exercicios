dep_ini=float(input("Qual o depósito inicial? "))
i=float(input("Taxa de juros da poupança: "))
mes=1
saldo_f=dep_ini
total_j=0
while mes<=24:
    
    saldo_f*=1+i
    
    print("Saldo do mês {0}: {1:.2f}".format(mes,saldo_f))
    
    mes=mes+1
total_j=saldo_f-dep_ini
print("Total de juros ganhos: {0:.2f}".format(total_j))   
    