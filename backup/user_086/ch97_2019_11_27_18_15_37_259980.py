def total_do_semestre_por_bairro(gastos_12meses):
    #gastos é um dicionário
    lista_12meses = gastos_12meses.values()
    gastos_6meses = {}
    for k in gastos_12meses.keys():
        i = 5
        soma = 0
        c=0
        while i<len(lista_12meses):
            print(i)
            while c<len(lista_12meses[i]):
                print(c)
                soma = soma + lista_12meses[i][c]
                print(soma)
                c+=1
            i+=1
        gastos_6meses[k] = soma
    return gastos_6meses