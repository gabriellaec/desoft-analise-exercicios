def calcula_media (lista):
    
    total = 0
    numero_alunos = 0
    
    for dici in lista:
        for nota in dici.values():
            total += nota
            numero_alunos += 1
            
    media = total/ numero_alunos
    return media 