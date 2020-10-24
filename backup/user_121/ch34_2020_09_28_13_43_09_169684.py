def eh_primo(teste):
  if teste==2:
    resultado=True
  elif teste%2==0 or teste==1 or teste==0:
    resultado=False
  else:
    i=2
    while i<teste:
      if teste%i==0:
        resultado=False
        break
      else:
        i+=1
      resultado=True
  return resultado

def maior_primo_menor_que(n):
  i=0
  if n>1:
    while i<=n:
      if eh_primo(i)==True:
        resultado=i
      i+=1
  else:
    resultado=-1
  return resultado