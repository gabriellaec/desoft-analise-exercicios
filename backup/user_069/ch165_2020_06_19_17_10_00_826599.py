def mais_populoso(pais):
    
    mais_populoso = ""
    maior_pop = 0
    
    for estado in pais:
        pop_total = 0

        for municipio in pais[estado]:
            pop_total += pais[estado][municipio]
            
            if pop_total > maior_pop:
                maior_pop = pop_total
                mais_populoso = estado
          
    return mais_populoso
                
                
        