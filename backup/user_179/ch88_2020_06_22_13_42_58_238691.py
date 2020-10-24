class Retangulo:
    def __init__(self, pie, psd):
        dx = psd.x - pie.x
        dy = psd.y - pie.y
    def calcula_perimetro(self,dx,dy):
        return (dx*2 + dy*2)
    def calcula_area(self,dx,dy):
        return (dx*dy)