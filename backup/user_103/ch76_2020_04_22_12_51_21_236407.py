def aniversariantes_de_setembro(dicionario):
    dicionario2={}
    for nome, nascimento in dicionario.items():
        if nascimento[4]=='9':
            dicionario2[nome]=nascimento
    return dicionario2
            
        
        
