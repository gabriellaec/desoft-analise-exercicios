def calcula_media(lista_notas):
    somatoria = 0
    lista_alunos = []
    for dicionarios in lista_notas:
        for aluno in dicionarios:
            somatoria += aluno
            lista_alunos.append(aluno) 
            
    
    media = somatoria / len(lista_alunos)
    return media