class Box:
    def __init__(self, centerX = 0.0, centerY = 0.0, centerZ = 0.0, width = 1.0, height = 1.0, depth = 1.0):
        self.centerX = centerX
        self.centerY = centerY
        self.centerZ = centerZ
        self.width = width
        self.height = height
        self.depth = depth
    
    def setCenter(self,x, y, z):
        self.centerX = x
        self.centerY = y
        self.centerZ = z
    
    def setWidth(self, width):
        self.width = width
    
    def setHeight(self, height):
        self.height = height

    def setDepth(self, depth):
        self.depth = depth

    def volume(self):
        return self.width*self.height*self.depth

    def surfaceArea(self):
        return 2*((self.width*self.depth)+(self.height*self.depth)+(self.height*self.width))

    def __repr__(self):
        return "{}-by-{}-by-{} 3D box with center at ({}, {}, {})".format(int(self.width),int(self.height),int(self.depth),self.centerX,self.centerY,self.centerZ)

    def touches(self, otherBox):
        xMax = self.centerX+(self.width/2)
        xMin = self.centerX-(self.width/2)
        yMax = self.centerY+(self.height/2)
        yMin = self.centerY-(self.height/2)
        zMax = self.centerZ+(self.depth/2)
        zMin = self.centerZ-(self.depth/2)
        x2Max = otherBox.centerX+(otherBox.width/2)
        x2Min = otherBox.centerX-(otherBox.width/2)
        y2Max = otherBox.centerY+(otherBox.height/2)
        y2Min = otherBox.centerY-(otherBox.height/2)
        z2Max = otherBox.centerZ+(otherBox.depth/2)
        z2Min = otherBox.centerZ-(otherBox.depth/2)
        if (xMin <= x2Max and x2Min <= xMax) and (yMin <= y2Max and y2Min <= yMax) and (zMin <= z2Max and z2Min <= zMax):
            return True
        else:
            return False

    def contains(self, otherBox ):
        xMax = self.centerX+(self.width/2)
        xMin = self.centerX-(self.width/2)
        yMax = self.centerY+(self.height/2)
        yMin = self.centerY-(self.height/2)
        zMax = self.centerZ+(self.depth/2)
        zMin = self.centerZ-(self.depth/2)
        x2Max = otherBox.centerX+(otherBox.width/2)
        x2Min = otherBox.centerX-(otherBox.width/2)
        y2Max = otherBox.centerY+(otherBox.height/2)
        y2Min = otherBox.centerY-(otherBox.height/2)
        z2Max = otherBox.centerZ+(otherBox.depth/2)
        z2Min = otherBox.centerZ-(otherBox.depth/2)
        if xMax > x2Max and xMin < x2Min and yMax > y2Max and yMin < y2Min and zMax > z2Max and zMin < z2Min:
            return True
        else:
            return False

import random
class NimGame:
    
    def __init__(self,myList):
        self.myList = myList
        print ("Nim game initialized with {} heaps.".format(len(myList)))
        
    def __repr__(self):
        print("<Nim game with {} heaps.".format(len(self.myList)))
        count = 0
        for x in self.myList:
            print("\tHeap {}: {} balls".format(count,x))
            count+=1
        return ">"

    def remove(self,heap,balls):
        if heap in range(len(self.myList)):
            if balls <= self.myList[heap] and self.myList[heap]!=0:
                self.myList[heap] = self.myList[heap]-balls
                print(self.myList)
                print("You took {} balls from heap {}".format(balls,heap))
                if self.gameOver() == True:
                    return "You Lost Computer Won"
                randHeap = random.randint(0,len(self.myList)-1)
                while self.myList[randHeap]==0:
                    randHeap = random.randint(0,len(self.myList)-1)
                randBalls = random.randint(1,self.myList[randHeap])
                self.myList[randHeap] = self.myList[randHeap]-randBalls
                print("Computer took {} balls from heap {}".format(randBalls,randHeap))
                if self.gameOver()==True:
                    return "You won!"
            else:
                return "You can't take away that many balls from heap {}".format(heap)
        else:
            return "there is no heap {}".format(heap)

    def gameOver(self):
        if all(v == 0 for v in self.myList):
            return True
        else:
            return False


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
