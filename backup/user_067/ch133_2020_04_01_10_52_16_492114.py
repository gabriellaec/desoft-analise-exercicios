resp = str(input('Está funcionando?'))
if(resp == 's'):
   print('Sem problemas!')
elif(resp=='n'):
   resp = str(input('Você sabe corrigir?(s/n)'))
   if(resp == 's'):
      print('Sem problemas!')
   elif(resp=='n'):
      resp=str(input('Você precisa corrigir? (s/n)'))
      if(resp=='s'):
        print('Apague tudoo e tente novamente')
      elif(resp=='n'):
        print('Sem problemas!')