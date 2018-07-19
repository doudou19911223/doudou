'''
# 导入包的所有内容，但只能执行__init__.py中的内容
from pkg01 import *

inInit()
'''
# 导入包中指定模块的所有内容
from pkg01.py01 import *
sayHello()
stu = Student()
stu.say()
