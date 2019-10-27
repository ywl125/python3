# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 20:30:44 2018

@author: alone
"""

   #class DerivedClassName(BaseClassName)
   #其中的BaseClassName为需要继承的基类父类或者超类
   #class DerivedClassName(Base1,Base2,Base3,Base4,...)
   #多重继承在括号类用逗号隔开多个基类名,尽量少用,容易错误
   
class Parent:
    def hello(self):
        print("正在调用父类的方法...")
        
class Child(Parent):
    pass

p=Parent()
p.hello()

c=Child()
c.hello()

import random as r

class Fish:
    def __init__(self):
        self.x=r.randint(0,10)
        self.y=r.randint(0,10)
        
    def move(self):
        self.x -=1
        print("我的位置是:",self.x,self.y)
        
class Goldfish(Fish):
    
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass

class Shark(Fish):
    def __init__(self): #子类 重写父类的方法,子类的方法就会替代父类,
      # Fish.__init__(self)  #在本子类下就会失去move方法,如果需要
        super().__init__()   #有两种方法实现.第一种是调用未绑定的
        self.hungry=True       #父类方法,第二种是使用super函数
     
        
        
    def eat(self):
        if self.hungry:
            print("吃货的梦想就是天天有吃不完的食物 ...")
            self.hungry=False
        else:
            print("吃的我好撑啊...")
            

