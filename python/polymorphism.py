class Vehicel:
    def __init__(self, name, year, model):
        self.name = name
        self.year=year
        self.model = model
    
    def getNameandModel(self):
        print(self.name, self.model)
        
class EV_car(Vehicel):
    pass


car1=Vehicel("name",'uyear','aurion')
ev = EV_car("toyota", "2007", "Aurion")


ev.getNameandModel()