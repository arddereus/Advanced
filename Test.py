class Point:
     def __init__(self, x=0, y=0):
         self.x = x
         self.y = y


     def distance_from_origin(self):
         return ((self.x ** 2) + (self.y ** 2)) ** 0.5

     def halfway(self, target):
         mx = (self.x + target.x)/2
         my = (self.y + target.y)/2
         return Point(mx, my)

     def slope_from_origin(self):
         sxo = (self.y)/(self.x)
         return sxo

# p1 = Point(10, 5)
# r = p1.slope_from_origin()
# print(r)

p2 = Point(20,10)
p3 = Point(80,20)
r1 = p2.halfway(p3)
print(r1.x, r1.y)


# #
# # #
# # # Point(4, 10).slope_from_origin()
# #
# # r = p1.halfway(p2)
# print(Point(3, 4).halfway(Point(5, 12)))

# class Rectangle:
#
#     def __init__(self, posn, w, h):
#         self.corner = posn
#         self.width = w
#         self.height = h
#
#     def __str__(self):
#         return "012"
#             .format(self.corner, self.width, self.height)
#
# box = Rectangle(Point(0, 0), 100, 200)
# bomb = Rectangle(Point(100, 80), 5, 10) # In my video game
# print("box: ", box)
# print("bomb: ", bomb)

