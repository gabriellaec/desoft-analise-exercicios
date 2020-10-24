class Circulo:
    def __init__(self,Pc,r):
        self.pc=Pc
        self.raio=r
    def contem(self,ponto):
        distancia=((self.x.pc-self.x.ponto)**2+(self.y.pc-self.y.ponto)**2)
        if distancia>self.raio:
            return False
        else:
            return True
        
        