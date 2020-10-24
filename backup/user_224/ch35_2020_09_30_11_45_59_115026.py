perguntas = True
s = 0
while perguntas :
     i = int(input('Digite um numero (Digite 0 para acabar com a soma): '))
     if i != 0 :
          i += int(input('Digite outro numero (Digite 0 para acabar com a soma): '))
          s += i
     else :
          perguntas = False
          print(s)