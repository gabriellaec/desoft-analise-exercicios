nao = [n,nao,Nao]
sim = [s,sim,Sim]
objeto_movimento = str(input('O objeto esta movendo? '))
if objeto_movimento in sim:
    mov2 = str(input('Deveria se mover? '))
    if mov2 in sim:
        print('Sem problemas!')
    elif mov2 in nao:
        print('Silver tape')
    else:
        print('Reponda com sim ou nao')
elif objeto_movimento in nao:
    objeto_parado = str(input('Deveria estar parado?'))
    if objeto_parado in sim:
        print('Sem problemas!')
    elif objeto_parado in nao:
        print('WD-40')