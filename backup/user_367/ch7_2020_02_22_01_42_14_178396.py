print('O Programa calcula área de um triângulo.' , '\n')
p_usuário = input('Valor da base: ')
r_usuário = input('Valor da altura: ')
if (p_usuário.isdigit() and r_usuário.isdigit()):
    p = float(p_usuário)
    r = float(r_usuário)

    a = p * r/2
    
    print()
    
    mensagem = ('Valor da aréa: ')
    print(a)
    
else:
    print('Um ou mais valores são inválidos.')
