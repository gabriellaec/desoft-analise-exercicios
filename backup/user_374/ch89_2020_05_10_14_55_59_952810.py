class Ponto:
    #essa classe vai receber dois pontos com x e y, ou seja, dois pares de coordenadas
    def __init__(self, x, y):
        #definindo o que é cada um
        self.x = x
        self.y = y

    def distancia_pontos(self, outro_ponto):
        #fazendo uuma função que calcula a distância entre dois pontos
        b = ((self.x - outro_ponto.x)**2 + (self.y - outro_ponto.y)**2)
        #retornando o valor da conta
        return b
#criando uma classe pra verificar o circulo
class Circulo:
    #definindo os parâmtros iniciais da função, centro do círculo e raio
    def __init__(self, centro, raio):
        self.centro =  centro
        self.raio = raio
    #verificando se o círculo contem algum ponto que vamos escolher, ou seja, se o ponto está dentro do círculo
    def contem(self, ponto):
        if self.centro.distancia_pontos(ponto) <= self.raio:
            #se estiver, então temos que retornar True
            return True
        else:
            #se não está, então retornamos False
            return False