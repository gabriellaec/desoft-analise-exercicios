programa=True
resposta=input('Está funcionando: ')
if resposta=='sim':
    programa=False
    print('Sem problemas')
while (programa):
    a=input('Você sabe corrigir? ')
    if a=='não':
        b=input('Você precisa corrigir? ')
    else:
        a=False
        input('Sem problemas')
    if b=='não':
        input('Sem problemas')
    else:
        input('Apague e tente novamente')
        
        
    