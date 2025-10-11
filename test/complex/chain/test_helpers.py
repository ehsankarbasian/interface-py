from unittest import TestCase

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.parent.absolute())
sys.path.append(path)

from interface import interface


@interface
class _Interface_1:
    field_1: int
    
    def method_1(self): """ The DocString """


@interface
class _Interface_2(_Interface_1):
    field_2: str = ...
    
    @staticmethod
    def static_method_2(param_1): ...
    
    @classmethod
    def class_method_2(cls): pass


@interface
class _Interface_3(_Interface_2):
    field_3: float
    
    def method_3(self, param_1): ...
    
    @property
    def property_3(self): """ The DocString """


@interface
class _Interface_4(_Interface_3):
    field_4: bool = ...
    
    def method_4(self): ...
    
    @staticmethod
    def static_method_4(): ...
    
    @property
    def property_4(self): pass


class ContractEnforceTestCase(TestCase):
    
    def setUp(self):
        self.Interface_2 = _Interface_2
        self.Interface_3 = _Interface_3
        self.Interface_4 = _Interface_4
    
    def tearDown(self):
        del self.Interface_2
        del self.Interface_3
        del self.Interface_4
    
    def assertContractError(self, context, expected_message_prefix, expected_contracts):
        error_message = str(context.exception)
        self.assertIn(expected_message_prefix, error_message)
        for contract_name in expected_contracts:
            self.assertIn(contract_name, error_message)
