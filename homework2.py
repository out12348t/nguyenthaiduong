# B1
# import math
# class Point2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"({self.x}, {self.y})"
    
#     def khoangcach(self, other):
#         diem1 = other.x - self.x
#         diem2 = other.y - self.y
#         return math.sqrt(diem1**2+diem2**2)

# class Point3D(Point2D):
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z

#     def __str__(self):
#         return f"({self.x}, {self.y}, {self.z})"
    
#     def khoangcach(self, other):
#         diem1 = other.x - self.x
#         diem2 = other.y - self.y
#         diem3 = other.z - self.z
#         return math.sqrt(diem1**2 + diem2**2 + diem3**2)
    
# #
# p2d1 = Point2D(1, 2)
# p2d2 = Point2D(5, 3)
# p3d1 = Point3D(1, 2, 3)
# p3d2 = Point3D(3, 1, 2)

# hello = Point2D.khoangcach(p2d1,p2d2)
# hello1 = Point3D.khoangcach(p3d1,p3d2)
# print(hello)
# print(hello1)

class WareHouse:
    maximumValue = 100
    def __init__(self, key, value):
        self.key = key
        self.value = int(value)
        def __str__(self):
            return f"({self.key}:{self.value})"
   
    def __str__(self):
        return f"({self.key}:{self.value})"

    def listItems(self,other):
        self.key = [self.value]    
        if self.key == other.key:
            return "mặt hàng đã có sẵn"
    # def getAllValues(self):
    # def addItem(self, name, value)
    # def removeItem(self, name, value)
    # def isFull(self)
     
    # def isEmpty(self)
