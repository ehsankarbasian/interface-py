from unittest import TestCase

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.parent.parent.absolute())
sys.path.append(path)

from interface import interface


@interface
class _Interface_1:
    field_1: int
    
    def method_1(self): """ The DocString """


@interface
class _Interface_2:
    field_2: str = ...
    
    @staticmethod
    def static_method_2(param_1): ...
    
    @classmethod
    def class_method_2(cls): pass


@interface
class _Interface_3:
    field_3: float
    
    def method_3(self, param_1): ...
    
    @property
    def property_3(self): """ The DocString """


@interface
class _Interface_4:
    field_4: bool = ...
    
    def method_4(self): ...
    
    @staticmethod
    def static_method_4(): ...
    
    @property
    def property_4(self): pass


_INTERFACE_CONTRACTS = {
    1: ['field_1', 'method_1'],
    2: ['field_2', 'static_method_2', 'class_method_2'],
    3: ['field_3', 'method_3', 'property_3'],
    4: ['field_4', 'method_4', 'static_method_4', 'property_4']
}

def _get_aggregated_contract(*args):
    aggregated = []
    for index in args:
        aggregated += _INTERFACE_CONTRACTS[index]
    
    return aggregated
    

class ContractEnforceTestCase(TestCase):
    
    def setUp(self):
        self.Interface_1 = _Interface_1
        self.Interface_2 = _Interface_2
        self.Interface_3 = _Interface_3
        self.Interface_4 = _Interface_4
    
    def tearDown(self):
        del self.Interface_1
        del self.Interface_2
        del self.Interface_3
        del self.Interface_4
