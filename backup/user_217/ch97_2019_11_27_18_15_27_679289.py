def total_do_semestre_por_bairro(gasto):
    
    gasto={
    'Bairro 1': [1234.45, 5123.32, 6134.35, 8567.98, 5472.28, 9715.38, 1380.15, 2569.42, 8459.24, 8351.25, 4082.19, 1750.16],
    'Bairro 2': [236.62, 845.52, 475.72, 846.22, 735.34, 846.26, 48.97, 624.37, 375.46, 4568.76, 73.32, 475.74],
    'Bairro 3': [51234.45, 5123.32, 61334.35, 8567.98, 5472.28, 9715.38, 1380.15, 2569.42, 8459.24, 82351.25, 4082.19, 1750.16],
    }

    for v in gasto['Bairro 1']:
        x = sum(gasto['Bairro 1'])
        
    
    for v in gasto['Bairro 2']:
        y = sum(gasto['Bairro 2'])
    
    for v in gasto['Bairro 3']:
        z = sum(gasto['Bairro 3'])
    
    gastos_por_bairro={'Bairro 1':x, 'Bairro 2': y,'Bairro 3':z}
    
    return gastos_por_bairro
    