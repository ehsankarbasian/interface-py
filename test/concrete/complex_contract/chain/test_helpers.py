from unittest import TestCase

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.parent.parent.absolute())
sys.path.append(path)

from src import interface


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


_CONTRACTS_LEVEL_1 = ['field_1', 'method_1']
_CONTRACTS_LEVEL_2 = ['field_2', 'static_method_2', 'class_method_2']
_CONTRACTS_LEVEL_3 = ['field_3', 'method_3', 'property_3']
_CONTRACTS_LEVEL_4 = ['field_4', 'method_4', 'static_method_4', 'property_4']

_ALL_CONTRACTS = {
    1: _CONTRACTS_LEVEL_1,
    2: _CONTRACTS_LEVEL_1 + _CONTRACTS_LEVEL_2,
    3: _CONTRACTS_LEVEL_1 + _CONTRACTS_LEVEL_2 + _CONTRACTS_LEVEL_3,
    4: _CONTRACTS_LEVEL_1 + _CONTRACTS_LEVEL_2 + _CONTRACTS_LEVEL_3 + _CONTRACTS_LEVEL_4
}

class ContractEnforceTestCase(TestCase):
    
    def setUp(self):
        self.Interface_2 = _Interface_2
        self.Interface_3 = _Interface_3
        self.Interface_4 = _Interface_4
    
    def tearDown(self):
        del self.Interface_2
        del self.Interface_3
        del self.Interface_4


class ContractEnforceLeveledTestCase(ContractEnforceTestCase):
    
    chain_level: int = ...
    expected_message_prefix: str = ...
    
    def setUp(self):
        self._assertChainLevelSettedCorrectly()
        self._assertExpectedMessagePrefixSettedCorrectly()
        
        return super().setUp()
    
    
    def _assertChainLevelSettedCorrectly(self):
        self.assertIsNotNone(self.chain_level)
        self.assertNotEqual(self.chain_level, Ellipsis)
        self.assertGreater(self.chain_level, 0)
        self.assertIsInstance(self.chain_level, int)
    
    
    def _assertExpectedMessagePrefixSettedCorrectly(self):
        self.assertIsNotNone(self.expected_message_prefix)
        self.assertNotEqual(self.expected_message_prefix, Ellipsis)
        self.assertIsInstance(self.expected_message_prefix, str)
    
    
    def assertContractError(self, context, expected_contracts):
        error_message = str(context.exception)
        normalized_error_message = error_message.replace(',', '').split(':')[-1].split()
        
        self.assertIn(self.expected_message_prefix, error_message)
        
        for contract_name in expected_contracts:
            self.assertIn(contract_name, normalized_error_message)
        
        exclude_contracts = [
            item for item in _ALL_CONTRACTS[self.chain_level] if item not in expected_contracts]
        if exclude_contracts:
            for contract in exclude_contracts:
                self.assertNotIn(contract, normalized_error_message, msg=error_message)
        
        self.assertNotIn('\n', error_message)
