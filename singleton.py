


class Singleton(type):
    def __new__(cls, name, bases, namespace):
        namespace['_instance'] = None
        return super(Singleton, cls).__new__(cls, name, bases, namespace)



class SingletonBase(metaclass=Singleton):

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Create new instance for class {}".format(cls.__name__))
            instanceof = super(SingletonBase, cls).__new__(cls)
            cls._instance = instanceof
            return instanceof
        else:
            print("The class {} has been instantiated".format(cls.__name__))
            return cls._instance




class MyClass(SingletonBase):
    def __init__(self,val):
        self._val = val



if __name__ == '__main__':
    x = MyClass(10)
    y = MyClass(20)
    print("pointer of x: {}".format(x))
    print("pointer of y: {}".format(y))
    assert x is y
    print("x._val: {}".format(x._val))
    print("y._val: {}".format(y._val))