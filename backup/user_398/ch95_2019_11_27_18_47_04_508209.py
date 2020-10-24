def mais_populoso(pais):
    dicionario={}
    for estado in pais :
        soma=0
        for municipio in pais[estado]:
            soma += pais[estado][municipio]
            
        dicionario[estado]=soma
        
    maior=0
    populoso=' '
    for estado in dicionario:
        if dicionario[estado]>maior:
            maior=dicionario[estado]
            populoso=estado
        
    return populoso