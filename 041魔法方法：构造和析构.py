# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 19:17:21 2018

@author: alone
"""

         #魔法方法总是被双下划线__包围，比如__init_()
         #在类定义时有时候需要__init_(self[,....])
         #原因在于类实例化的时候需要调用__init__(self[,....])
         #默认是没有参数
         #如果你定义的类需要一个或多个参数，那么在定义类的时候
         #需要对__init__(self[,....])进行初始化重构操作
         
class Rectangle:
    def __init__(self,x,y):
        self.x=x  #self.x代表类实例化之后的对象，右边的x指传入的参数
        self.y=y
        
    def getperi(self):
        return(self.x+self.y)*2
        
    def getarea(self):
        return self.x*self.y
    
        #如果需要对传入的参数进行修改，那么就需要在定义类的时候
        #在实例化参数前，对参数进行重新修改用到如下方法
        # __new__(cls[,...])
    
class Capstr(str):   #这个例子是把传入的字符串都变为大写
    def __new__(cls,string):
        string=string.upper()#调用字符串方法把字符变为大写
        return str.__new__(cls,string)
    
       #__del__(self)方法，只在python垃圾回收机制启动的时候启用
       
class C:
    def __init__(self):
        print('我是__init__方法，我被调用了。。。。')
    def __del__(self):
        print('我是__del__方法，我被调用了。。。。')
        
  # a=C()  此时调用的是__init__方法
  #del a     此时调用的是__del__方法

         