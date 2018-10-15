class A():
    def __init__(self):
        self.__name='python' #翻译成self._A__name='python'
    
class A(A): #派生类和基类取相同的名字就可以使用基类的私有变量。
    def func(self):
        print(self.__name) #翻译成print self._A__name

instance=A()
instance.func()
