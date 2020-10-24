dinheiro = 1000
p1=input("QUer apostar?")
if p1=='não':
    print("Acabou o jogo")
while p1=='sim':
    import random
    num1=random.randit(1,6)
    num2=random.randit(1,6)
    chute=input("Chute um numero")
    