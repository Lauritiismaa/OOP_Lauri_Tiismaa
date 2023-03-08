class Seade:
    
    
    def __init__(self,TooteKood,Nimetus,Hindilmakm):
        self.TooteKood = TooteKood
        self.Nimetus = Nimetus
        self.Hindilmakm = Hindilmakm
        self.kmhind = self.Hindilmakm * 0.2 + self.Hindilmakm
    
    def setTooteKood(self,TooteKood):
        self.TooteKood = TooteKood
    def getTooteKood(self):
        return self.TooteKood
    
    
    def setNimetus(self,Nimetus):
        self.Nimetus = Nimetus
    def getNimetus(self):
        return self.Nimetus
    
    
    def setHindilmakm(self,Hindilmakm):
        self.Hindilmakm = Hindilmakm
    def getHindilmakm(self):
        return self.Hindilmakm
    
    
    def kmhind(self):
        (self.Hindilmakm) * 0.2 + (self.Hindilmakm)
        print("Hind koos käibemaksuga on " + str(kmhind) + " eurot")
        
    def tekstiks(self):
        print("Tootekood on:",self.TooteKood,", Toote nimetus on:",self.Nimetus,
              ", Hind ilma käibemaksuta on:",self.Hindilmakm,", Hind koos käibemaksuga on",self.kmhind)
        
        
SeadeYks = Seade(372890,"Telefon",200)
SeadeKaks = Seade(647329,"Arvuti",800)