
def calcula_valor_devido(valor_emprestado,taxa_de_juros,num_meses):
    valor_devido = valor_emprestado*(1+(taxa_de_juros/100))**(num_meses)
    print(' O valor devido e de {0} reais'.format(valor_devido))
    
        
	
    