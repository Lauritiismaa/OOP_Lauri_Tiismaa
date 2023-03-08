#Lauri Tiismaa IT-21 07.03.2023

class inimene:


    def __init__(self, nimi, vanus):
        self.nimi = nimi
        self.vanus = vanus
        
        
    def vanane(self, vana):
        self.vanus = vana + self.vanus
        print("Teie uus vanus on: " + str(self.vanus))
        
        
class opilane(inimene):
    
    
    def __init__(self, nimi, vanus, ryhm, keskminehinne, energia):
        super().__init__(nimi, vanus)
        self.ryhm = ryhm
        self.keskminehinne = keskminehinne
        self.energia = energia
        
        
    def opi(self):
        if self.energia > 30:
            self.keskminehinne = 0.1 + self.keskminehinne
            print("Teie keskmine hinne tõusis 0.1 võrra!")
            print("Teie uus keskmine hinne on: " + str(self.keskminehinne))
        else:
            print("Teil ei ole piisavalt energiat, et õppida!!")
            
    
    def puhka(self, tund):
        self.energia = (tund * 10) + self.energia
        print("magasid " + str(tund) + " tundi")
    
    
class opetaja(inimene):
    
    
    def __init__(self, nimi, vanus, energia):
        super().__init__(nimi, vanus)
        self.energia = energia
        
        
    def opeta(self):
        if self.energia > 20:
            print("Hakkasite õpetama!")
        else:
            print("Teil ei ole piisavalt energiat, et õpetada!")
            
            
    def puhka(self, tund):
        self.energia = (tund * 10) + self.energia
        print("magasid " + str(tund) + " tundi")
        
        
opilane = opilane("juku", 14, "7B", 3.2, 100)
opetaja = opetaja("maimu", 60, 80)
opilane.vanane(1)
opilane.opi()
opilane.puhka(2)
opetaja.opeta()
opetaja.puhka(1)