def mais_populoso(pais):
    maiorpop=0
    maiorest=""
    for estado in pais:
        i=0
        for municipio in pais[estado]:
            i+=pais[estado][municipio]
            if i>maiorpop:
                maiorpop=i
                maiorest=estado
                
            
           
            