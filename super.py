#Super() = function used to give access to the methods of the parent class.
#          returns a temporary object of the parent class when used

class rect:
    def __init__(self, leng, wid):
        self.leng = leng
        self.wid = wid

class square(rect):
    def __init__(self,leng,wid):
        super().__init__(leng,wid)
    def area(self):
        return self.wid * self.leng

class cube(rect):
    def __init__(self,leng,wid,height):
        super().__init__(leng,wid)
        self.height = height
    def volume(self):
        return self.wid * self.leng *self.height

square = square(3,3)
cube = cube(3,3,3)

print(square.area())
print(cube.volume())
