import math

x = 0
maior_diferença = 0
while x<90:
    seno_bhaskara = (4*x*(180-x)) / (40500-x*(180-x))
    seno = math.sin(x)
    if abs(seno_bhaskara-seno) > maior_diferença:
        maior_diferença = abs(seno_bhaskara-seno)
        ângulo = x
    x+=1
    
print(ângulo)
    