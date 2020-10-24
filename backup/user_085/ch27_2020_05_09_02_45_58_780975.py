x = True
while x:
  resposta_do_aluno = input('Está com dúvidas? ')
  if resposta_do_aluno != 'não':
    print('Pratique mais')
  else:
    print('Até a próxima')
    x = False