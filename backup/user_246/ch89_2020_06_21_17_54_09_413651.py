class Circulo:
    def __init__(self, c, r):
        self.raio = r
        self.centrox = c.x
        self.centroy = c.y
    def contem(self, ponto):
        x = ponto.x
        y= ponto.y
        r=self.raio
        cx=self.centrox
        cy=self.centroy
        maxi = r+cx
        mini = cx - r
        ma = r+cy
        mi = cy-r
        if maxi > x and x > mini and ma>y and y>mi:
            return True
        else:
            return False