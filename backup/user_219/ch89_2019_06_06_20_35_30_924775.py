class Circulo:
    def __init__(self,Centro, raio):
        self.centrox= Centro.x
        self.centroy= Centro.y 
        self.raio= raio
    def contem(self,ponto):
        self.pontox= ponto.x
        self.pontoy=ponto.y
        if ((self.centrox - self.pontox)**2 + (self.centroy - self.pontoy)**2)> (self.raio)**2
            return False
        else:
            return True
            