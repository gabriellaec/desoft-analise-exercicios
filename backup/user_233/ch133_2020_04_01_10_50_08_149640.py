def fluxograma():
    
    funcionando = input()
    if funcionando == 's': return 'Sem problemas!'
    if funcionando != 'n': return 'Nadaver'
    
    sabe_corrigir = input()
    if sabe_corrigir == 's': return 'Sem problemas!'
    if sabe_corrigir != 'n': return 'Nadaver'
    
    precisa_corrigir = input()
    if precisa_corrigir == 's': return 'Apague tudo e tente novamente'
    if precisa_corrigir != 'n': return 'Nadaver'
    
    return 'Sem problemas!'

print(fluxograma())
    