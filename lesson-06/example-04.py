class Point:
    """Class  for create and set coord"""

    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.getAttrs()
        self.checkAttrs()
    
    def getAttrs(self):
        print(f"Get Attrs: {self.__dict__}")

    def checkAttrs(self):
        for attr in self.__dict__:
            # print(getattr(self, attr))
            if getattr(self, attr) < 0:
                print("Attribute cannot be less than 0")
                setattr(self, attr, 0)
            elif getattr(self, attr) > 100:
                print("Attribute cannot be more than 100")
                setattr(self, attr, 100)
        print(f"Check Attrs: {self.__dict__}")

    def setAttrs(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.getAttrs()
        self.checkAttrs()
        print(f"Set Attrs: {self.__dict__}")

coord_01 = Point(-1, 101, 50)
coord_01.setAttrs(-111, 222, -333)
coord_01.setAttrs(11, 22, 33)
