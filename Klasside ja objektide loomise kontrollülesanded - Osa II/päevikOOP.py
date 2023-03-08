#Lauri Tiismaa IT-21 22.02.2023

class sissekanne:
    
   
   def __init__ (self, sissekandetyyp, sissekandevarv, kuupaev, tundidearv, hinne):
       self.sissekandetyyp = sissekandetyyp
       self.sissekandevarv = sissekandevarv
       self.kuupaev = kuupaev
       self.tundidearv = tundidearv
       self.hinne = hinne
       
       
       def andmed(self):
            print("teie sissekandetüüp on: ", self.sissekandetyyp, "teie sissekandearv on: ", self.sissekanderarv, "kuupaev on: ", self.kuupaev, "teie tundide arv on: ", self.tundidearv, "Teie hinne on: ", self.hinne)
        
        
        def muudahinnet(self, hinded):
            if hinne < 5:
                self.hinne = hinded
                print("Uus hinne on: ", hinne,"Teie hinne on:", self.hinne)
                else:
                    print("Sellist hinnet ei saa sisse kanda!!!")
        
        
        def muudatyyp(self, sissekandetyyp, sissekandearv):
            self.sissekandetyyp = sissekandetyyp
            self.sissekandevarv = sissekandevarv
            print("Sissekande tüüp vahetati", sissekandetyyp, "Nüüd on sissekandetüüp", self.sissekandetyyp)
            print("sissekande värv vahetati", sissekandevarv, "Nüüd on sissekandevärv", self.sissekandevarv)
        
        
sissekanneyks = sissekanne("praktiline töö", "roheline", "22.02.2023", 4, 5)
sissekannekaks = sissekanne("kotrolltöö", "punane", "22.02.2023", 3, 2)
sissekanneyks.andmed()
sissekannekas.andmed()
sissekanneyks.muudahinnet(2)
sissekannekaks.muudatyyp("tunnikontroll", "roheline")