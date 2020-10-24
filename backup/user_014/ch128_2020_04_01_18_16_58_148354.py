movimento = input('O objeto está se movendo? (s/n) ')

if movimento == 's':
    deveria_se_mover = input('Deveria se mover? (s/n) ')
    if deveria_se_mover == 's':
        print('"Sem problemas!"')
    else:
        print('"Silver tape"')        
else: #movimento == 'n'
    deveria_estar_parado = input('Deveria estar parado? (s/n) ')
    if deveria_estar_parado == 's':
        print ('"Sem problemas!"')
    else:
        print ('"WD-40"')