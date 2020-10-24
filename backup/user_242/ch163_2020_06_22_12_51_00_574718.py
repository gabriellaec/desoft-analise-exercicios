def calcula_media(alunos):
    contador = 0 
    soma = 0
    for aluno in alunos:
        contador = 0 
        for nota in aluno.values():
            soma+= nota
            contador += 1
            media = soma/contador        
    return media
                
