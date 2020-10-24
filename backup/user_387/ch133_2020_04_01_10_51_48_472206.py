resposta = input('O programa está funcionando? (n/s)')
if resposta == 's':
    print('Sem problemas!')

elif resposta == 'n':
    resposta = input('Você sabe corrigir? (n/s)')

if resposta == 's':
    print('Sem problemas!')

elif resposta == 'n':
    resposta = input('Você precisa corrigir? (n/s)')

if resposta == 's':
    print('Apague tudo e tente novamente')

elif resposta == 'n':
    print('Sem problemas!')