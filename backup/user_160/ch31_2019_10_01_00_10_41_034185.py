def emprest(valor,salario,quantanos):
    prestacao = valor/quantanos*12
    if prestacao <= 0.3*salario:
        print("Empréstimo aprovado")
        else:
            print ("Empréstimo não aprovado")
