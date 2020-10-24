x = 0
diferença = 0
while x<90:
    seno_bhaskara = (4*x*(180-x)) / (40500-x*(180-x))
    seno = math.sin(x)
    nova_diferença = seno_bhaskara - seno
    if abs(nova_diferença)>diferença:
        diferença = nova_diferença
        valor = x
    x+=1
print(valor)
    