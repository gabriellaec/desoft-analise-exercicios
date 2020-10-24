import random
n1=random.randint(0,100)
n2=random.randint(0,100)
n3=random.randint(0,100)
if n1<n2<n3:
    print ('crescente')
elif n1>n2>n3:
    print ('decrescente')
else:
    print ('nenhum')