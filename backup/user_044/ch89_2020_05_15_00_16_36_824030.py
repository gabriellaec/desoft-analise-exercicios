class Circulo:
    def __init__(self,Pc,r):
        self.pc=Pc
        self.raio=r
    def contem(self,ponto):
        self.ponto=ponto
        distancia=((self.pc.x-self.ponto.x)**2+(self.pc.y-self.ponto.y)**2)
        if distancia>self.raio:
            return False
        else:
            return True
        
        