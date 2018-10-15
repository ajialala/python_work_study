class A():
    def __init__(self):
        self.__name='python' #私有变量，翻译成 self._A__name='python'
    def __say(self): #私有方法,翻译成 def _A__say(self)
        print(self.__name) #翻译成 self._A__name
    
a=A()
#print a.__name #访问私有属性,报错!AttributeError: A instance has no attribute '__name'
print(a.__dict__) #查询出实例a的属性的集合
print(a._A__name) #这样，就可以访问私有变量了
#a.__say()#调用私有方法，报错。AttributeError: A instance has no attribute '__say'
print(dir(a))#获取实例的所有属性和方法
a._A__say() #这样，就可以调用私有方法了
'''
从上面看来,python还是非常的灵活，它的oop没有做到真正的不能访问，只是一种约定让大家去遵守，
比如大家都用self来代表类里的当前对象，其实，我们也可以用其它的，只是大家习惯了用self  
'''
