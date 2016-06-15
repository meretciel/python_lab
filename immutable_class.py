
# In this script, we will implement an Immutable class.
# The implementation is developed with Python 3. In order to run the code with Python2.7, we need to change the
# __setattr__ function in ImmutableBase to _setattribute__ function .


class ImmutableMeta(type):
    def __new__(cls, name, bases, namespace):
        namespace['_instances'] = []
        return super(ImmutableMeta, cls).__new__(cls, name, bases, namespace)


class ImmutableBase(metaclass=ImmutableMeta):

    def __setattr__(self, name, val):
        if self in self._instances:
            raise Exception("The class is immutable.")
        self.__dict__[name] = val

    def __getattribute__(self, item):
        if item == '__dict__' and self in self._instances:
            raise Exception("Not allowed to access __dict__.")
        return super(ImmutableBase, self).__getattribute__(item)

    def __init__(self):
            self._instances.append(self)

class MyImmutableClass(ImmutableBase):
    def __init__(self, x):
        self.x = x
        super(MyImmutableClass, self).__init__()



if __name__ == '__main__':
    instanceof = MyImmutableClass(10)
    instanceof.x = 200



