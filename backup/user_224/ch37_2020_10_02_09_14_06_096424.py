programa = True

palavra = str(input('Qual a senha? '))

while programa :
     if palavra != 'desisto' :
         palavra = str(input('Senha incorreta.Tente novamente : '))
     else:
          programa = False
          print('Você acertou a senha!')
        