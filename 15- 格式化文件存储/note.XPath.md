# XPath
- 在XML文件中查找信息的一套规则/语言，根据XML的元素或者属性进行遍历
- http://www.w3school.com.cn/xpath/index.asp
# XPath开发工具
- 开源的XPath表达式编辑攻击：XMLQuire
- Chrome插件：XPath Helper
- Firefox插件：XPath Checker
 
 # 选取节点
 - nodename：选取此节点的所有子节点
 - /：从根节点开始选取
 
        /Student:没有结果
        /School:选取School节点
 - //:选取节点，不考虑位置
 
        //age:选取出一个节点，一般组成列表返回
        
 - .:选取当前节点
 - ..:选取当前节点的父亲节点
 - @：选取属性
 - xpath中查找一般按照路径方法查找
        School/Teacher:返回Teacher节点
        School/Student:返回两个Student节点
        //Student:选取所有Student的节点，不考虑位置
        School//Age:选取School后代中所有的Age节点
        //@other:选取other属性
        //Age[@Detail]:选取带有属性Detail的Age元素
        
# 谓语-predicates
- /School/Student[1]:选取School下面的第一个Student节点
- /School/Student[last()]:选取School下面的最后一个Student节点
- /School/Student[last()-1]:选取School下面的倒数第二个一个Student节点
- /School/Student[position()<3]: 选取School下面的前二个Student节点
- //Student[@score]: 选取带有属性score的Student节点
- //Student[@score="99"]: 选取带有属性score并且属性值是99的Student节点
- //Student[@score]/Age: 选取带有属性score的Student节点的子节点Age

# xpath的一些操作
- |：或者
        //Student[@score] | //Teacher:选取带有属性score的Student节点
 
- 其余不常见XPath运算符号包括+，-， div， >, < 
        