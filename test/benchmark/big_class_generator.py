import itertools

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.absolute())
sys.path.append(path)

from interface import interface, concrete, InterfaceBase
from abc import ABC, abstractmethod


_unique_counter = itertools.count(0)

def make_big_interface(num_fields=100, num_methods=100, with_annotations=True):
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
    g = {"InterfaceBase": InterfaceBase}
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
    g = {"ABC": ABC, "abstractmethod": abstractmethod}
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
