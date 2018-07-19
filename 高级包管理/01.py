# 包含一个学生类，
# 一个sayhello函数
# 一个打印语句

class Student():
    def __init__(self,name="NoName",age=18):
        self.name = name
        self.age = age
    def say(self):
        print("My name is {0},age is {1}。".format(self.name,self.age))

def sayHello():
    print("hello,我是图灵学院")
print("你好，找我什么事？")