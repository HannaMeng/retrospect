#-*-coding:utf-8 -*-
#@author:HM
#斐波那契数列

#1.计算前n项斐波那契数列
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a+b
        n = n + 1
    return 'done'
fib(6)
#
#2.计算小于n之前的斐波那契数列
def fib(max):
    a,b = 0,1
    while b < max:
        print(b)
        a,b = b,a+b
    return 'done'
fib(6)

