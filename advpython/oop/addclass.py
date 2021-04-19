class add:
  def addval(self,no1,no2):
      self.no1=no1
      self.no2=no2
  def printadd(self):
      print("sum =",self.no1+self.no2)
obj=add()
obj.addval(50,20)
obj.printadd()