x = 0
diferenças = []
while x<90:
    seno_bhaskara = (4*x*(180-x)) / (40500-x*(180-x))
    seno = math.sin(x)
    diferenças.append(abs(seno_bhaskara-seno))
    x+=1
    
print(max(diferenças))
    