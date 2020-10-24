class Circulo:
    def __init__(self):
        self.centrox = centrox
        self.centroy = centroy
        self.raio = raio
    
    def contem(self, ponto):
        parteX = abs(self.centrox - Ponto.x)
        parteY = abs(self.centroy - Ponto.y)
        
        dist = (parteX**2+parteY**2)**(1/2)
        
        if dist <= self.raio:
            print('O ponto está dentro da área do círculo')
            
        else:
            print('O ponto não está dentro da área do círculo')