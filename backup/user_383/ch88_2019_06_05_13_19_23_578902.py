class Retangulo:
	def __init__(self, superiordireito = Point(x,y), inferioresquerdo = Point(x,y))
    	self.superiordireito = superiordireito        
        self.inferioresquerdo = inferioresquerdo
        self.lado = superiordireito.x - inferioresquerdo.x
        self.altura = superiordireito.y - inferioresquerdo.y
    def calcula_perimetro(self):
        self.perimetro = (self.lado + self.altura)*2
        return self.perimetro
    
    def calcula_area(self):
        self.area = self.lado * self.altura
        return self.area
    
rect = Retangulo(Ponto(x,y),Ponto(x,y))
