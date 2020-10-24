programa = True

while programa :
     palavra = str(input('Qual a senha? '))
     if palavra != 'desisto' :
     palavra = str(input('Qual a senha? '))
     else:
          programa = False
          print('Você acertou a senha!')
          