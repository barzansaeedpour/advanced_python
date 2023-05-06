"""
    Singleton
        - Ensure a class only has one instance, and provide a global point of access to it.
"""

# first method:

from typing import Any


class A:
    _instance = None

    def __init__(self):
        raise RuntimeError('call get_instance() instead')
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)

        return cls._instance


# to test:
try:
    one = A()
except:
    pass 

one = A.get_instance()
two = A.get_instance()

# the ids should be the same

print(id(one))
print(id(two))

# #########################################################

# second method (using meta classes):

class Singleton(type):
    _instance = None

    def __call__(self, *args: Any, **kwds: Any):
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance
    
class A(metaclass= Singleton):
    pass

one = A()
two = A()






