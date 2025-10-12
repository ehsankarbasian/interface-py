from unittest import TestCase

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.parent.parent.absolute())
sys.path.append(path)

from src import interface


@interface
class _Interface_1:
    field_1: int
    
    @property
    def property_1(self): pass


@interface
class _Interface_2(_Interface_1):
    
    def method_2(self, param_1): ...
    
    @classmethod
    def class_method_2(cls): pass
    
    @property
    def property_2(self): ...


@interface
class _Interface_3:
    
    def method_3(self): pass
    
    @property
    def property_3(self): ...


@interface
class _Interface_4(_Interface_3):
    field_4: bool = ...
    
    @staticmethod
    def static_method_4(param_1, param_2): pass
    
    @property
    def property_4(self): ...


@interface
class _Interface_5(_Interface_2, _Interface_3):
    field_5: float
    
    def method_5(self, a, b): pass
    
    @property
    def property_5(self): """Docstring only"""


@interface
class _Interface_6:
    field_6: bytes = ...
    
    @property
    def property_6(self): ...


@interface
class _Interface_7(_Interface_6):
    
    def method_7(self): ...
    
    @staticmethod
    def static_method_7(param_1): pass
    
    @property
    def property_7(self): """Docstring only"""


@interface
class _Interface_8(_Interface_4, _Interface_7):
    field_8: dict = ...
    
    def method_8(self, x): """Docstring only"""
    
    @property
    def property_8(self): pass


@interface
class _Interface_9(_Interface_5, _Interface_6):
    field_9: complex
    
    def method_9(self): ...
    
    @property
    def property_9(self): pass


_INTERFACE_CONTRACTS = {
    1: ['field_1', 'property_1'],
    2: ['method_2', 'class_method_2', 'property_2'],
    3: ['method_3', 'property_3'],
    4: ['field_4', 'static_method_4', 'property_4'],
    5: ['field_5', 'method_5', 'property_5'],
    6: ['field_6', 'property_6'],
    7: ['method_7', 'static_method_7', 'property_7'],
    8: ['field_8', 'method_8', 'property_8'],
    9: ['field_9', 'method_9', 'property_9']
}


class ContractEnforceTestCase(TestCase):
    
    def setUp(self):
        # self.Interface_1 = _Interface_1
        self.Interface_2 = _Interface_2
        # self.Interface_3 = _Interface_3
        self.Interface_4 = _Interface_4
        self.Interface_5 = _Interface_5
        # self.Interface_6 = _Interface_6
        self.Interface_7 = _Interface_7
        self.Interface_8 = _Interface_8
        self.Interface_9 = _Interface_9
    
    
    def tearDown(self):
        # del self.Interface_1
        del self.Interface_2
        # del self.Interface_3
        del self.Interface_4
        del self.Interface_5
        # del self.Interface_6
        del self.Interface_7
        del self.Interface_8
        del self.Interface_9
