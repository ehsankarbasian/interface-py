import time
import itertools
from memory_profiler import memory_usage

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.absolute())
sys.path.append(path)

from interface import interface, concrete, InterfaceBase
from abc import ABC, abstractmethod


def bench_time_and_memory(label, fn, n=1):
    """Run fn() n times measuring time and memory peak"""
    start = time.perf_counter()
    for _ in range(n):
        fn()
    dur = time.perf_counter() - start

    def wrapper():
        for _ in range(n):
            fn()

    mem_samples = memory_usage(wrapper, max_iterations=1)
    mem_peak_mib = (max(mem_samples) - min(mem_samples))
    print(f"{label:40s}: {dur:.4f} sec for {n} runs, +{mem_peak_mib:.4f} MiB peak memory")


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


_unique_counter = itertools.count(0)

def make_big_interface(num_fields=100, num_methods=100, with_annotations=True):
    """
    Returns the created interface
    """
    index = next(_unique_counter)
    cls_name = f"BigInterface_{num_fields}f_{num_methods}m_{index}"

    lines = [f"class {cls_name}(InterfaceBase):"]
    for i in range(num_fields):
        if with_annotations:
            if i % 2 == 0:
                lines.append(f"    field_{i}: int")
            else:
                lines.append(f"    field_{i}: int = ...")
        else:
            lines.append(f"    field_{i} = ...")

    for j in range(num_methods):
        lines.append(f"    def method_{j}(self): ...")

    src = "\n".join(lines)
    # global namespace for exec
    g = {
        "InterfaceBase": InterfaceBase,
    }
    # exec the class definition
    local_vars = {}
    exec(src, g, local_vars)
    cls = local_vars[cls_name]
    cls = interface(cls)
    return cls


def make_big_abc(num_fields=0, num_methods=100, with_annotations=True):
    index = next(_unique_counter)
    cls_name = f"BigABC_{num_fields}f_{num_methods}m_{index}"

    lines = [f"class {cls_name}(ABC):"]
    for j in range(num_methods):
        lines.append(f"    @abstractmethod")
        lines.append(f"    def method_{j}(self): ...")

    src = "\n".join(lines)
    g = {
        "ABC": ABC,
        "abstractmethod": abstractmethod,
    }
    local_vars = {}
    exec(src, g, local_vars)
    cls = local_vars[cls_name]
    return cls


def make_big_concrete_from_interface(iface_cls):
    index = next(_unique_counter)
    cls_name = f"ConcreteImpl_{iface_cls.__name__}_{index}"
    lines = [f"class {cls_name}({iface_cls.__name__}):"]

    annotations = getattr(iface_cls, "__annotations__", {})
    ellipsis_fields = [k for k, v in iface_cls.__dict__.items() if v is Ellipsis and not k.startswith("__")]
    field_names = set(annotations.keys()) | set(ellipsis_fields)

    for field_name in sorted(field_names):
        lines.append(f"    {field_name} = 1")

    method_names = [k for k, v in iface_cls.__dict__.items() if callable(v) and not k.startswith("__")]
    for m in sorted(method_names):
        if m.startswith("method_") or m.startswith("f") or m in ("do",):
            lines.append(f"    def {m}(self):")
            lines.append(f"        return 1")

    src = "\n".join(lines)
    g = {iface_cls.__name__: iface_cls}
    local_vars = {}
    exec(src, g, local_vars)
    cls = local_vars[cls_name]
    cls = concrete(cls)
    return cls


def make_big_abc_impl(abc_cls):
    index = next(_unique_counter)
    cls_name = f"ABCImpl_{abc_cls.__name__}_{index}"
    lines = [f"class {cls_name}({abc_cls.__name__}):"]
    method_names = [k for k, v in abc_cls.__dict__.items() if callable(v) and not k.startswith("__")]
    
    for m in method_names:
        lines.append(f"    def {m}(self):")
        lines.append(f"        return 1")
    
    src = "\n".join(lines)
    g = {abc_cls.__name__: abc_cls}
    local_vars = {}
    exec(src, g, local_vars)
    cls = local_vars[cls_name]
    return cls


if __name__ == "__main__":
    # small quick baseline
    N = 10000
    bench_time_and_memory("Interface definition (small)     ", make_interface_class, n=N)
    bench_time_and_memory("Concrete definition (small)      ", make_concrete_class, n=N)
    bench_time_and_memory("ABC definition (small)           ", make_abc_class, n=N)
    bench_time_and_memory("ABC implementation (small)       ", make_abc_impl, n=N)

    print("\n\n------ Large-class benchmarks (time + memory) ------\n")

    # sizes: list of (fields, methods, iterations)
    sizes = [
        (50, 50, 200),    # lite
        (200, 200, 200),  # medium
        (800, 800, 200),   # heavy
    ]

    for num_fields, num_methods, iterations in sizes:
        label_interface = f"Interface {num_fields} fields / {num_methods} methods"
        label_abstract = f"ABC       {num_methods} methods"

        bench_time_and_memory(label_interface.ljust(50),
                              lambda: make_big_interface(num_fields,
                                                         num_methods,
                                                         with_annotations=True),
                              n=iterations)
        bench_time_and_memory((label_interface + " -> concrete").ljust(50),
                              lambda: make_big_concrete_from_interface(make_big_interface(num_fields,
                                                                                          num_methods,
                                                                                          True)),
                              n=iterations)

        bench_time_and_memory(label_abstract.ljust(50),
                              lambda: make_big_abc(0, num_methods, True),
                              n=iterations)
        bench_time_and_memory((label_abstract + " -> implementation").ljust(50),
                              lambda: make_big_abc_impl(make_big_abc(0, num_methods, True)),
                              n=iterations)
        print()

    print("Done.")
