# 所有以双下划线开始的名字都被"翻译"成前面加上单下划线和类名的形式。
class A(object):
	def __init__(self):
		self.__data=[]  #翻译成 self._A__data=[]
	def add(self,item):
		self.__data.append(item) #翻译成 self._A__data.append(item)
	def printData(self):
		print (self.__data)  #翻译成 self._A__data

a=A()
a.add('hello')
a.add('python')
a.printData()
a.__data = 'hhhhhhhh'
a.__ddd = 222
#print a.__data  #外界不能访问私有变量 AttributeError: 'A' object has no attribute '__data'
print(a._A__data) #通过这种方式，在外面也能够访问“私有”变量；这一点在调试中是比较有用的！
print(a.__data)
print(a.__dict__) # 获取实例的所有属性
print(dir(a)) # 获取实例的所有属性和方法
