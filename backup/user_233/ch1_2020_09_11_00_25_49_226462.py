def calcula_valor_devido(valor, meses, taxa):
    ''' 
        Calcula juros compostos mensais sobre um
        'valor' ao longo de x 'meses'
        a uma 'taxa' específica.
        
        Retorna os juro devido somado ao valor inicial.
        
        calcula_valor_devido(valor, meses, taxa) -> valor + juro total
        
        taxa em porcentagem (10 = 10%)
    '''
    
    return valor * (1 + taxa) ** meses