from random import randint
dinheiro=1000
desejo=input("Deseja apostar?")
while desejo!="não":
    dado1=randint(1,6)
    dado2=randint(1,6)
    soma=dado1+dado2
    chute1=input("Qual o seu chute?")
    dinheiro-=30