class Rectangle:

    def __init__(self, posn, w, h):
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return ("{0},{1},{2}".format(self.corner, self.width, self.height))

    def area(self):
        return (self.height)*(self.width)

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

box = Rectangle(Point(0,0), 100, 200)
bomb = Rectangle(Point(100,80), 5, 10)


print("box:", box)
print(box.area())
