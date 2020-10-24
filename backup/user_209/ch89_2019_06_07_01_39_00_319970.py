class Circulo:
    def __init__ (self, centro, raio):
    	self.cx = centro.x 
        self.cy = centro.y
        self.raio = raio
    
    def contem(self,ponto):
        self.px = ponto.x
        self.py = ponto.y
        distancia = (((self.px - self.cx)**2) + (self.py - self.cy)**2)**0.5
        if distancia > self.raio:
            dentro = False
        else:
            dentro = True
   		return dentro