class SerVivo:
    def _init_(self):
        self.pontos_de_vida = 100
        self.ataque = 10
    
    def atacar(self, outro_ser_vivo):
        outro_ser_vivo.pontos_de_vida -= self.ataque
        if outro_ser_vivo.pontos_de_vida <= 0:
            print("Você venceu!")

class Personagem(SerVivo):
    def _init_(self, nome):
        self.nome = nome 


class Monstro(SerVivo):
    def _init_(self, tipo):
        self.tipo = tipo

class Lobo(Monstro):
    def _init_(self, forca):
        super()._init_("Lobo")
        self.forca = forca

class Glodin(Monstro):
    def _init_(self, inteligencia):
        super()._init_("Glodin")
        self.inteligencia = inteligencia