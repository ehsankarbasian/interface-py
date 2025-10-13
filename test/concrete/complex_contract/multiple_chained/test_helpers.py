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


__INTERFACE_CONTRACTS = {
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

def __get_contract_aggregate(*indexes):
    result = []
    
    for index in indexes:
        result += __INTERFACE_CONTRACTS[index]
    
    return result


class _HashableList(list):
    
    def __hash__(self):
        value = ''.join([str(item) for item in self])
        return int(value)


_AGGREGATED_CONTRACTS = {
    _HashableList([2, 4]): __get_contract_aggregate(1, 2, 3, 4),
    _HashableList([2, 4, 7]): __get_contract_aggregate(1, 2, 3, 4, 6, 7),
    _HashableList([5, 7]): __get_contract_aggregate(1, 2, 3, 5, 6, 7),
    _HashableList([5, 8]): __get_contract_aggregate(1, 2, 3, 4, 5, 6, 7, 8),
    _HashableList([4, 9]): __get_contract_aggregate(1, 2, 3, 4, 5, 6, 9),
    _HashableList([4, 7, 9]): __get_contract_aggregate(1, 2, 3, 4, 5, 6, 7, 9),
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


class ContractEnforceMultipleChainedTestCase(ContractEnforceTestCase):
    
    expected_message_prefix: str = ...
    # self.current_interfaces: list[int]
    
    def setUp(self):
        self._assertExpectedMessagePrefixSettedCorrectly()
        return super().setUp()
    
    def __setattr__(self, name, value):
        if name == "current_interfaces":
            value = _HashableList(value)
        return super().__setattr__(name, value)
    
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
            self.assertGreaterEqual(9, item)
    
    @property
    def _aggregated_contracts(self):
        return _AGGREGATED_CONTRACTS[self.current_interfaces]


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
