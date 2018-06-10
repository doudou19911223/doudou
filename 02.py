
#print
print(19)
class Student():
    name = "dana"
    age = 18
    # 注意say的写法，参数由一个self
    def say(self):
        self.name = "aaaa"
        self.age = 200
        print("my name is {0}".format(self.name))
        print("my age is {0}".format(self.age))
yueyue = Student()
yueyue.say()