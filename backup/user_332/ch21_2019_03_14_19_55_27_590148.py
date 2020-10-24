def valor_da_conta(conta):
    
    total = conta * 1.1
    
    return("Valor da conta com 10%: R$ {0:.2f}".format(total))
    
conta = float(input("Quanto foi sua conta?"))

print(valor_da_conta(conta))