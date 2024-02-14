#         Method overloading      -->    compile-time Polymorphism
'''
class asd:
    def add(self, a, b):  # This will not work
        print(a + b)
    
    def add(self, a, b, c):
        print(a + b + c)
obj=asd()
obj.add(1,2,3)#6
obj.add(1,2)#error
'''
#         Method overriding     -->   Run-time Polymorphism
'''
class asd:
    def add(self,a,b):
        print(a+b)
class sdf(asd):
    def add(self,a,b,c):
        print(a+b+c)
obj=sdf()
obj.add(1,2,3)#6
obj.add(1,2)#error
'''
#         Method overloading     -->    run-time Polymorphism
'''
class asd:
    def add(self,a,b,c=0):
        print(a+b+c)
obj=asd()
obj.add(1,2,3)
'''
#       Operator Overloading    -->      Run-time polymorphism     or    dynamic polymorphism 
'''
class asd:
    def add(self,a,b):
        print(a+b)
    def __add__(self,other):
        print("This is addition")
class sdf(asd):
    def sub(self,a,b):
        print(a-b)
obj1=asd()
obj2=sdf()
obj1.add(11,12)
obj2.sub(12,11)
obj2+obj1
'''
#                    Abstraction

'''

from abc import ABC,abstractmethod
class c1(ABC):
    @abstractmethod
    def add(self,a,b):
        print(f'{a}+{b} = {a+b}')
    def sub(self,a,b):
        print(a-b)
class c2(c1):
    def add(self,a,b):  # This method is necessary as we use this as abstractmethod in parent class
        super().add(a,b)
    def sub(self,a,b):
        print(f'{a}-{b} = {a-b}')
        
obj=c2()
obj.add(13,12)
obj.sub(13,12)
'''




















    
        


            
