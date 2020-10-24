def calcula_media(alunos):
    contador = 0 
    soma = 0
    for i in alunos:
        contador = 0 
        for v in ai.values():
            soma+= v
            contador += 1
            media = soma/contador        
    return media
                
