# a sample class
# class partyanimal:
#     x = 0
#     def party(self):
#         self.x = self.x +2
#         print("so_far",self.x)
# an = partyanimal()
# an.party()
# an.party()
# ------------------------
# class partyanimal:
#     x = 0
#     name = ""
#     def __init__(self,z,b):
#         self.name = z
#         self.x = b
#         print(self.name,"constructed")
#     def party(self):
#         self.x = self.x + 1
#         print (self.name,"partly_count",self.x)
# q =partyanimal("quincy",2)
# # m = partyanimal("mia")
# q.party()
# ------------------
# class complex_number():
#     def __init__(self,f,s):
#         self.first = f
#         self.second = s
#     def comput_num(self):
#         x = self.first * self.second
#         print x
# resutl = complex_number(7,8)
# resutl.comput_num()
#-----------------------------
# class Dog:
#     def __init__(self,name):
#         self.name = name
#         self.tricks = []
#     def add_trick(self,trick):
#         self.tricks.append(trick)
#         print trick
# d = Dog('jim')
# d.add_trick('roll_over')
# d.tricks
# b = Dog('tam')
# b.add_trick('hoo hoo')
# b.tricks
# # ----------------------------
# class bag():
#     def __init__(self):
#         self.data = []
#     def add(self,x):
#         self.data.append(x)
#     def add_twice(self,x):
#         self.add(x)
#         self.add(x)
#         print(self.data)
# an = bag()
# an.add_twice(2)
# ------------------------------
class partlyanimal():
    x = 0
    name = ""
    def __init__(self,nam):
        self.name = nam
    def party(self):
        self.x = self.x + 1
        print (self.name,self.x)
class footballfan(partlyanimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name,self.points)
j = footballfan("jim")
j.touchdown()
b = footballfan("sally")
b.touchdown()

