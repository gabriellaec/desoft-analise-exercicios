
def calcula_media(alunos):
    
    soma_notas = 0
    qtde_alunos = 0
    
    for dicionario in alunos:
        soma_notas += sum(dicionario.values())
        qtde_alunos += len(dicionario)
    
    return soma_notas / qtde_alunos



