class Retangulo():
    def __init__(self,Ponto(x,y),Ponto(z,w)):
        self.ponto1=Ponto(x,y)
        self.ponto2=Ponto(z,w)
    def calcula_perimetro(self):
        Perimetro=(ponto2.x-ponto1.x)*2+(Ponto2.y-ponto1.y)*2
        return Perimetro
    
    def calcula_area(self):
        Area=(ponto2.x-ponto1.x)*(ponto2.y-ponto1.x)
        return Area