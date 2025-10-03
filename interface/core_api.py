from .core import InterfaceMeta as _InterfaceMeta


def _interface(cls):
    cls._is_interface_ = True
    cls.__validate__()
    return cls


@_interface
class InterfaceBase(metaclass=_InterfaceMeta):
    pass


def interface(cls):
    if not issubclass(cls, InterfaceBase):
        raise TypeError(
            f"Interface class '{cls.__name__}' must inherit from InterfaceBase "
            f"(did you forget to add 'InterfaceBase' as a base class?)"
        )
    
    cls._is_interface_ = True
    cls.__validate__()
    return cls


def concrete(cls):
    cls._is_interface_ = False
    cls.__validate__()
    return cls
