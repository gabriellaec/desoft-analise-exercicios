class Ponto:
    #essa classe vai receber dois pontos com x e y, ou seja, dois pares de coordenadas
    def __init__(self, x, y):
        #definindo o que é cada um
        self.x = x
        self.y = y


class Retangulo:
    #classe que vai fazer cálculos com base em um retângulo
    def __init__(self, p1, p2):
        #definindo os pontos
        self.pie = p1
        self.psd = p2

    def calcula_perimetro(self):
        #retomando o método de x e y definindo na classe ponto
        b = self.psd.x - self.pie.x
        a = self.psd.y - self.pie.y
        return 2*(a+b) 
    
    def calcula_area(self):
        b = self.psd.x - self.pie.x
        a = self.psd.y - self.pie.y
        return a*b

