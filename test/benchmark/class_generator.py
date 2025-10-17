import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.absolute())
sys.path.append(path)

from src.interface_py import interface, concrete
from abc import ABC, abstractmethod


@interface
class FooInterface:
    x: int
    
    def do(self): ...
    
    @staticmethod
    def s(): ...
    
    @property
    def y(self): ...


@concrete
class ConcreteFoo(FooInterface):
    x: int = 10
    
    def do(self):
        return 42
    
    @staticmethod
    def s():
        return "ok"
    
    @property
    def y(self):
        return "y"


class AbstractFoo(ABC):
    @abstractmethod
    def do(self): ...
    
    @abstractmethod
    def s(self): ...
    
    @property
    @abstractmethod
    def y(self): ...


class ConcreteFooABC(AbstractFoo):
    
    def do(self):
        return 42
    
    def s(self): 
        return "ok"
    
    @property
    def y(self):
        return "y"


def make_interface_class():
    
    @interface
    class FakeInterface:
        a: int
        
        def f(self): ...
        
    return FakeInterface


def make_concrete_class():
    
    class FakeConcrete(ConcreteFoo):
        pass
    
    return FakeConcrete


def make_abc_class():
    
    class FakeABC(ABC):
        
        @abstractmethod
        def f(self): ...
        
    return FakeABC


def make_abc_impl():
    class ConcreteFakeABC(make_abc_class()):
        
        def f(self):
            return 1
        
    return ConcreteFakeABC
