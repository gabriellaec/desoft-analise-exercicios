from random import randint 
sorteio=randint(0,36)
print ("Dinheiro disponível: 100")
d=100
a=int(input("Sua aposta:")
if a==0:
      break
b=input("A aposta é em um número (num) ou paridade?")
if b=="num":
      n=int(input("Escolha um número de 1 a 36:")
      if n==sorteio:
              d=d+35*a
      else:
              d=d-a
if b=="paridade":
        pi=input("É par(p) ou ímpar(i)?")
        if pi=="i" and sorteio%2!=0:
            d=d+a
        elif pi=="p" and sorteio%2==0:
            d=d+a
        else:
            d=d-a
if d==0:
            print("Você perdeu")
        
              
              
              