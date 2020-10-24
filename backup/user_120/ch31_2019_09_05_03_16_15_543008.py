def emprestimo_banc(valor_casa,salario,anos_pag):
    prest=valor_casa/anos_pag/12
    if prest>salario*0.3:
    	return 'Empréstimo não aprovado'
    else:
    	return 'Empréstimo aprovado'