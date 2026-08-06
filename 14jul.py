# class Password:
    
#     def __init__(self,value):
#         Password.islong(value)
#         Password.isdigit(value)
#         self.value = value
        
#     @staticmethod
#     def islong(value):
#         return len(value) >= 8
#     @staticmethod
#     def isdigit(value):
#         for i in value:
#             return i.isdigit()
# print(Password.isdigit('aasasasa'))
class Circle:
    def __init__(self,rad):
        self.rad = rad
        
    def d(self):
        return self.rad * 2
    @property
    def s(self):
        return 3.14 * self.rad * self.rad
circle1 = Circle(10)
print(circle1.d())
print(circle1.s)
circle1.rad = 5
print(circle1.d())



