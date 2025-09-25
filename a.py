from interface import interface, concrete, InterfaceBase


@interface
class MyInterface(InterfaceBase):
    
    @property
    def foo(self):
        return "bar"
