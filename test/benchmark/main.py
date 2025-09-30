import time

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.absolute())
sys.path.append(path)

from interface import interface, concrete, InterfaceBase
from abc import ABC, abstractmethod


# Interface
@interface
class FooInterface(InterfaceBase):
    x: int
    def do(self): ...
    @staticmethod
    def s(): ...
    @property
    def y(self): ...


@concrete
class ConcreteFooInterface(FooInterface):
    x: int = 10
    def do(self): return 42
    @staticmethod
    def s(): return "ok"
    @property
    def y(self): return "y"


# Abstract Base Class
class AbstractFoo(ABC):
    @abstractmethod
    def do(self): ...
    @abstractmethod
    def s(self): ...
    @property
    @abstractmethod
    def y(self): ...

class ConcreteFooABC(AbstractFoo):
    def do(self): return 42
    def s(self): return "ok"
    @property
    def y(self): return "y"


# Benchmark Printer
def benchmark(label, fn, n=10000):
    start = time.perf_counter()
    for _ in range(n):
        fn()
    dur = time.perf_counter() - start
    print(f"{label}: {dur:.4f} sec for {n} runs")


def make_interface_class():
    @interface
    class FakeInterface(InterfaceBase):
        a: int
        def f(self): ...
    return FakeInterface

def make_concrete_class():
    @concrete
    class FakeConcrete(ConcreteFooInterface):
        pass
    return FakeConcrete

def make_abc_class():
    class FakeABC(ABC):
        @abstractmethod
        def f(self): ...
    return FakeABC

def make_abc_impl():
    class ConcreteFakeABC(make_abc_class()):
        def f(self): return 1
    return ConcreteFakeABC


# Run benchmark
if __name__ == "__main__":
    N = 10000
    benchmark("Interface definition", make_interface_class, n=N)
    benchmark("Concrete definition", make_concrete_class, n=N)
    benchmark("ABC definition", make_abc_class, n=N)
    benchmark("ABC impl", make_abc_impl, n=N)
