class dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title()+" "+"is sit")

    def roll_over(self):
        print(self.name+"is roll_over")

    def update(self,mile):
        self.age = mile
    def read(self):
        return self.age
    def increase(self):
        self.age += 1

class littledog(dog):
    def __init__(self,name,age):
        super().__init__(name,age)

dog1 = littledog("jiezhang",24)
print(dog1.read())
num = "jljkjahs"
# str.center(num)
dog1.increase()
print(dog1.read())

str1 = "helelo world"
str3 = "e"
print(str1.isspace())
print(str1.find(str3,0,len(str1)))
# print()
print(str1.capitalize())
# print(str1.join(str3))
str2 = list(str1)
print(str2)
for i in range(0,len(str2)):
    if str2[i] == ' ':
        str2[i] = '%20'
print(''.join(str2))
