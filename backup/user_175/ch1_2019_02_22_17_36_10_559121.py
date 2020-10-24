def calcula_valor_devido(valor_emprestimo, num_meses, valor_taxa_juros):
    valor_devido = (valor_emprestimo*((1 + valor_taxa_juros)**(num_meses)))
    return valor_devido
