
class Animal ():
    
    numAnimals = 0

    def __init__ (self, name = 'NoName', numLegs = 0):
        self.name = name
        self.numLegs = numLegs
        Animal.numAnimals = Animal.numAnimals + 1
        self.id = Animal.numAnimals

    def setName(self, name):
        self.name = name
        
    def getName(self):
        return self.name
    
    def getNumLegs(self):
        return self.numLegs
   
    def speak(self):
        print("...")

    def __repr__(self):
        return ('<{} the animal. ID:{}>'.format(self.name, self.id))

class Cat(Animal):
    def __init__(self, name = 'noname', furColor = 'unknown'):
        Animal.__init__(self, name, 4)
        self.color = furColor
    
    def speak(self):
        print('meow')

    def getFurColor(self):
        return self.color

    def __repr__(self):
        return ('<{} the {} cat. ID: {}>'.format(self.name, self.color, self.id))

class Dog(Animal):
    
    def __init__(self, name = 'rover'):
        Animal.__init__(self, name, 4)
    
    def speak(self):
        print('woof')
        
    def fetch(self):
        print("I'm fetching ...")

    def __repr__(self):
        return '<{} the dog. ID:{}>'.format(self.name, self.id)

class Snake(Animal):
    def __init__(self, name = "ozzy", species = 'unknown'):
        Animal.__init__(self, name, 0)
        self.species = species
    def speak(self):
        print("sssssssssssssssssssssssssssssssssssssssssssssss")

    def getSpecies(self):
        return self.species

    def sliter(self):
        print("I'm ssssssslithering")

    def __repr__(self):
        return '<{} the snake. ID:{}>'.format(self.name, self.id)


        
def testAnimal():
    c1 = Cat("Milo")
    c2 = Cat(furColor = "black")
    d1 = Dog()
    d2 = Dog()
    a1 = Snake()
    a2 = Snake(species = "Ball Python")
    for animal in [c1, c2, d1, d2, a1, a2]:
        print(animal)
        animal.speak()
    d1.fetch()
    a1.sliter()
    print(c2.getFurColor())
    print(a2.getSpecies())
