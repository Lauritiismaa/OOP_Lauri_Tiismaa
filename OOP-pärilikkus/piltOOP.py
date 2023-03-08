#Lauri Tiismaa IT-21 22.02.2023


class pilt:
    
    
    def __init__ (self, nimi):
        self.nimi = nimi
        
        
    def valjastanimi(self):
        print("Teie pildi nimi on: ", self.nimi)
    
    
class vektorpilt(pilt):
    
    
    def __init__ (self, nimi, formaat):
        super().__init__(nimi)
        self.formaat = formaat
        
        
    def valjastaformaat(self):
        print ("Formaat on:", self.formaat)


class rasterpilt(pilt):
    
    
    def __init__ (self, nimi, formaat, pikslid):
        super().__init__(nimi)
        self.formaat = formaat
        self.pikslid = pikslid


    def valjastaandmed(self):
        print("Teie pildi formaat on ", self.formaat, ", Teie pildil on piksleid: ", self.pikslid)
    
    
piltyks = pilt("madise pilt")
piltkaks = vektorpilt("Kivi pilt", "lai formaat")
piltkolm = rasterpilt("Peko pilt", "kitsas formaat", 1000)


piltyks.valjastanimi()
piltkaks.valjastaformaat()
piltkaks.valjastanimi()
piltkolm.valjastaandmed()
piltkolm.valjastanimi()