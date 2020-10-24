resposta=str('Responda com s ou n as respostas a seguir:)
print(resposta)
pergunta1=int(input('Está se movendo? '))
if pergunta1='n':
    pergunta2=int(input('Deveria estar parado? '))
    if pergunta2='n':
        print('WD-40')
    else:
        print('Sem problemas!)
else:
    pergunta3=int(input('Deveria se mover? '))
    if pergunta3='n':
        print('Silver tape')
    else:
        print('Sem problemas')
              

