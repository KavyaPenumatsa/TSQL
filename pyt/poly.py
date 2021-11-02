class Animal:
    def __init__(self,name):
        self.name=name
    def talk(self):
        print('Animal')
class Dog(Animal):
    def talk(self):
        print('Woof')
class Cat(Animal):
    def talk(self):
        print('Meow')
c=Cat('kitty')
c.talk()
d=Dog(Animal)
d.talk()
a=Animal('Animal')
a.talk()
a=d
a.talk()