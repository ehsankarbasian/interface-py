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


@interface
class _Interface_3:
    
    def method_3(self): pass
    
    @staticmethod
    def static_method_3(param_1): pass


@interface
class _Interface_4(_Interface_3):
    field_4: bool = ...


@interface
class _Interface_5(_Interface_2, _Interface_3):
    
    @classmethod
    def class_method_5(cls, a, b): pass
    
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


@interface
class _Interface_8(_Interface_4, _Interface_7):
    field_8: dict = ...
    
    @property
    def property_8(self): pass


@interface
class _Interface_9(_Interface_5, _Interface_6):
    field_9: complex
    
    def method_9(self): ...


__INTERFACE_CONTRACTS = {
    1: ['field_1', 'property_1'],
    2: ['method_2'],
    3: ['method_3', 'static_method_3'],
    4: ['field_4'],
    5: ['class_method_5', 'property_5'],
    6: ['field_6', 'property_6'],
    7: ['method_7', 'static_method_7'],
    8: ['field_8', 'property_8'],
    9: ['field_9', 'method_9']
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
        self.Interface_2_4 = (_Interface_2, _Interface_4)
        self.Interface_2_4_7 = (_Interface_2, _Interface_4, _Interface_7)
        self.Interface_5_7 = (_Interface_5, _Interface_7)
        self.Interface_5_8 = (_Interface_5, _Interface_8)
        self.Interface_4_9 = (_Interface_4, _Interface_9)
        self.Interface_4_7_9 = (_Interface_4, _Interface_7, _Interface_9)
    
    
    def tearDown(self):
        del self.Interface_2_4
        del self.Interface_2_4_7
        del self.Interface_5_7
        del self.Interface_5_8
        del self.Interface_4_9
        del self.Interface_4_7_9
    
    
    @property
    def current_interfaces(self):
        return self._current_interfaces
    
    @current_interfaces.setter
    def current_interfaces(self, value):
        assert isinstance(value, tuple)
        self._interface_indexes = _HashableList([
            int(item.__name__.split('_')[-1]) for item in value])
        self._current_interfaces = value
    
    @current_interfaces.deleter
    def current_interfaces(self):
        del self._interface_indexes
        del self._current_interfaces


class ContractEnforceMultipleChainedTestCase(ContractEnforceTestCase):
    
    expected_message_prefix: str = ...
    # self.current_interfaces: self.Interface_n_m
    
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
        self.assertTrue(hasattr(self, '_current_interfaces'))
        self.assertIsNotNone(self.current_interfaces)
        self.assertNotEqual(self.current_interfaces, Ellipsis)
        self.assertIsInstance(self.current_interfaces, tuple)
        for item in self._interface_indexes:
            self.assertIsInstance(item, int)
            self.assertGreater(item, 0)
            self.assertGreaterEqual(9, item)
    
    @property
    def _aggregated_contracts(self):
        return _AGGREGATED_CONTRACTS[self._interface_indexes]


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
