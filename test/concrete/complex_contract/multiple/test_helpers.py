from unittest import TestCase

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.parent.parent.absolute())
sys.path.append(path)

from src.interface_py import interface


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


class ContractEnforceMultipleTestCase(ContractEnforceTestCase):
    
    expected_message_prefix: str = ...
    # self.current_interfaces: list[int]
    
    def setUp(self):
        self._assertExpectedMessagePrefixSettedCorrectly()
        return super().setUp()
    
    
    def tearDown(self):
        self._assertCurrentInterfaces()
        del self.current_interfaces
        return super().tearDown()
    
    
    def _assertExpectedMessagePrefixSettedCorrectly(self):
        self.assertIsNotNone(self.expected_message_prefix)
        self.assertNotEqual(self.expected_message_prefix, Ellipsis)
        self.assertIsInstance(self.expected_message_prefix, str)
    
    
    def _assertCurrentInterfaces(self):
        self.assertTrue(hasattr(self, 'current_interfaces'))
        self.assertIsNotNone(self.current_interfaces)
        self.assertNotEqual(self.current_interfaces, Ellipsis)
        self.assertIsInstance(self.current_interfaces, list)
        for item in self.current_interfaces:
            self.assertIsInstance(item, int)
            self.assertGreater(item, 0)
            self.assertGreaterEqual(4, item)
    
    
    @property
    def _aggregated_contracts(self):
        aggregated = []
        for index in self.current_interfaces:
            aggregated += _INTERFACE_CONTRACTS[index]
        
        return aggregated
    
    
    def assertContractError(self, context, expected_contracts):
        error_message = str(context.exception)
        normalized_error_message = error_message.replace(',', '').split(':')[-1].split()
        
        self.assertIn(self.expected_message_prefix, error_message)
        
        for contract_name in expected_contracts:
            self.assertIn(contract_name, normalized_error_message)
        
        exclude_contracts = [
            item for item in self._aggregated_contracts if item not in expected_contracts]
        if exclude_contracts:
            for contract in exclude_contracts:
                self.assertNotIn(contract, normalized_error_message, msg=error_message)
        
        self.assertNotIn('\n', error_message)
