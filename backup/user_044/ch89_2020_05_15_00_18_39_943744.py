class Circulo:
    def __init__(self,Pc,r):
        self.Pc=Pc
        self.raio=r
    def contem(self,ponto):
        self.ponto=ponto
        distancia=((self.Pc.x-self.ponto.x)**2+(self.Pc.y-self.ponto.y)**2)**(1/2)
        if distancia>self.raio:
            return False
        else:
            return True
        
        