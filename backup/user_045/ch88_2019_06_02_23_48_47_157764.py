class Retangulo:
    def __init__(self,ponto1,ponto2):
        x1=ponto1.x
        y1=ponto1.y
        x2=ponto2.x
        y2=ponto2.y
    def calcula_perimetro(self):
        return (x1-x2)*2+(y1-y2)*2     
    def calcula_area(self):
        return (x1-x2)*(y1-y2)     