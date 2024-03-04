print("hello from python on ugfhfghfghgfhfbuntu on windowsgrgfgrrttttttttttttttt!")
l = input("Enter length")
b = input("Enter breadth")
print("Length is"+l)
print("Breadth is"+b)

def parameter(l,b):
    return l+b

def area(l,b):
    return l*b

linInt = int(l)
binInt = int(b)

print("Parameter is"+ str(parameter(linInt,binInt)))
print("Area is"+ str(area(linInt,binInt)))

class Triangle:
    def __init__(self,a,b,c):
       self.a = a
       self.b = b
       self.c = c
    
    def parameter(self):
        print(self.a+self.b+self.c)

    def area(self):
        print(0.5*self.b*self.a)

t1 = Triangle(2,3,5)
t2 = Triangle(0,5,45)

t1.area()
t1.parameter()
t2.area()
t2.parameter()
