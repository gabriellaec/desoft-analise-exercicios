class Circulo:
    def __init__(self, centrox, centroy, raio):
        self.centrox = centrox
        self.centroy = centroy
        self.raio = raio
    
    def contem(self, ponto):
        parteX = abs(self.centrox - ponto.x)
        parteY = abs(self.centroy - ponto.y)
        
        dist = (parteX**2+parteY**2)**(1/2)
        
        if dist <= self.raio:
            print('O ponto está dentro da área do círculo')
            
        else:
            print('O ponto não está dentro da área do círculo')
            
circulo = Circulo(0,0,2.3)

ponto = Ponto(2,2)

print(circulo.contem(ponto))