programa = True

while programa :
     palavra = input('Qual a senha? ')
     if palavra != 'desisto' :
     palavra = input('Qual a senha? ')
     else:
          programa = False
          print('Você acertou a senha!')
          