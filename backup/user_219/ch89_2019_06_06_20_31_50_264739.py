classe Circulo:
    def __init__(self,Centro, raio):
        self.centrox= Centro.x
        self.centroy= Centro.y 
        self.raio= raio
    def contem(self,ponto):
        self.pontox= ponto.x
        self.pontoy=ponto.y
        if ((self.centrox- self.pontox)**2+ (self.centroy-self.pontoy)**2)**0.5<= self.raio
            return True
        else:
            return False
            