class Veh:
    def __init__(self,model,rs):
        self.model=model
        self.rs=rs
    def printdata(self):
        print("model yr :",self.model)
        print("price :",self.rs)
class Bus(Veh):
    def __init__(self,type,model,rs):
        super().__init__(model,rs)
        self.type=type
    def printtype(self):
        print("Its a",self.type,"Vehicle ")
obj=Bus(2017,250000,"BS6")
obj.printdata()
obj.printtype()
