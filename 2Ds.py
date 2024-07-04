import math

class shape2D:
    def __init__(self,name,Doc):
        self.name = name
        self.Doc = Doc

class rectangle(shape2D):
    def __init__(self,name,Doc,leng,wid):
        super().__init__(name, Doc)
        self.leng = leng
        self.wid = wid
    def area(self):
        return self.wid*self.leng
    def peri(self):
        return (self.wid*2) + (self.leng*2)

class circle(shape2D):
    def __init__(self,name,Doc,rad):
        super().__init__(name, Doc)
        self.rad = rad
    def area(self):
        return self.rad * self.rad * math.pi

rect = rectangle("Rectangle","12-1-2022",4,5)
circle = circle("Circle","23-5-2002",7)

print("This is a "+ rect.name+". It was created on "+rect.Doc)
print("The area of the "+rect.name+" is "+str(rect.area()))
print("The perimeter of the "+rect.name+" is "+str(rect.peri()))

print("----------------------------------------")

print("This is a "+circle.name+". It was created on "+circle.Doc)
print("The area of the "+circle.name+" is "+str(circle.area()))