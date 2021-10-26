class box:
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

    def touches(self, otherBox):
        return

    def contains(self, otherBox ):
        return
        