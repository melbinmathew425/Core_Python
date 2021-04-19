class Parent():
    def phone(self):
        print("i have a Nokia")
class Child(Parent):
    def phone(self):
        print(" i have an Iphone")
ch=Child()
ch.phone()