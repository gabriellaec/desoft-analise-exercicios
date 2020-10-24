atleta = ''
maior = 0
while atleta != 'sair':
    atleta = input()
    if atleta != 'sair':
        acel = float(input())
        if acel > maior:
            maior = acel
            vencedor = atleta
print('O vencedor é '+atleta+' com tempo de conclusão de {0:.1f} s'.format(math.sqrt(200/maior)))