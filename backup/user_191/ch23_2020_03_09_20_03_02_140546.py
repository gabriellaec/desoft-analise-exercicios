v=int(input('velo'))
if v>80:
      p=(v-80)*5
      print('{0:.2f}'.format(p))
else:
      print('Não foi multado')