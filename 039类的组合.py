# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 19:56:36 2018

@author: alone
"""

class Turtle:
    def __init__(self,x):
        self.num=x
        
class Fish:
    def __init__(self,x):
        self.num=x
        
class Pool:
    def __init__(self,x,y):
        self.turtle=Turtle(x)
        self.fish=Fish(y)
        
    def print_num(self):
        print('水池里总共有乌龟 %d 只，小鱼 %d 条！' % (self.turtle.num,self.fish.num))
        
        
        
a=Pool(10,20)
a.print_num()

