class Circulo:
    def __init__(self, p1, p2):
        self.x=p1.x
        self.y=p1.y
        self.raio=p2
       
    def contem(self, ponto):
        if (self.x-p1.x)**2+(self.y-p1.y)**2<=self.raio**2:
            return True
        else:
            return False
        	