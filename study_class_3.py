# 小漏洞：派生类和基类取相同的名字就可以使用基类的私有变量
class A():
    def __init__(self):
        self.__name='python' #翻译成self._A__name='python'
    
class B(A):
    def func(self):
        print(self.__name) #翻译成print self._B__name

instance=B()
#instance.func()#报错：AttributeError: B instance has no attribute '_B__name'
print(instance.__dict__)
print(instance._A__name)
