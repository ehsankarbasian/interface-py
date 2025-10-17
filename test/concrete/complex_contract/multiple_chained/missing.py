import unittest

import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent.parent.resolve()
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from interface_py import concrete
from test.concrete.complex_contract.multiple_chained.test_helpers import ContractEnforceMultipleChainedTestCase


class MultipleInterfaceSuccessTestCase(ContractEnforceMultipleChainedTestCase):
    
    expected_message_prefix = "Concrete class 'Concrete' must implement contracts"
    
    
    def test_missing_24_1(self):
        self.current_interfaces = self.Interface_2_4
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(*self.current_interfaces):
                
                field_4 = None
                
                @property
                def property_1(self):
                    return 26
                
        expected_contracts = ['field_1', 'method_2', 'method_3', 'static_method_3']
        self.assertContractError(context, expected_contracts)
    
    
    def test_missing_24_2(self):
        self.current_interfaces = self.Interface_2_4
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(*self.current_interfaces):
                
                field_1 = 1
                
                @staticmethod
                def static_method_3(param_1):
                    ...
        
        expected_contracts = ['field_4', 'property_1', 'method_2', 'method_3']
        self.assertContractError(context, expected_contracts)
    
    
    def test_missing_24_3(self):
        self.current_interfaces = self.Interface_2_4
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(*self.current_interfaces):
                
                @property
                def property_1(self):
                    return 26
                
                def method_3(self):
                    ...
                
        expected_contracts = ['field_1', 'field_4', 'method_2', 'static_method_3']
        self.assertContractError(context, expected_contracts)
    
    
    def test_missing_247_1(self):
        
        self.current_interfaces = self.Interface_2_4_7
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(*self.current_interfaces):
                
                field_4 = True
                field_6 = b'aaa'
                
                def method_2(self, param_1):
                    pass
                
                @staticmethod
                def static_method_3(param_1):
                    ...
                
                @property
                def property_6(self):
                    return 26
                
        expected_contracts = ['field_1', 'property_1', 'method_3', 'method_7', 'static_method_7']
        self.assertContractError(context, expected_contracts)
    
    
    def test_missing_247_2(self):
        
        self.current_interfaces = self.Interface_2_4_7
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(*self.current_interfaces):
                
                field_1 = None
                field_4 = True
                
                @property
                def property_1(self):
                    ...
                
                @staticmethod
                def static_method_3(param_1):
                    ...
                
                @staticmethod
                def static_method_7(param_1):
                    pass
        
        expected_contracts = ['field_6', 'method_2', 'method_3', 'property_6', 'method_7']
        self.assertContractError(context, expected_contracts)
    
    
    def test_missing_247_3(self):
        
        self.current_interfaces = self.Interface_2_4_7
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(*self.current_interfaces):
                
                field_1 = None
                field_6 = b'aaa'
                
                def method_2(self, param_1):
                    pass
                
                def method_3(self):
                    ...
                
                def method_7(self):
                    ...
        
        expected_contracts = ['field_4', 'property_1', 'static_method_3', 'property_6', 'static_method_7']
        self.assertContractError(context, expected_contracts)
    
    
    def test_missing_57_1(self):

        self.current_interfaces = self.Interface_5_7
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(*self.current_interfaces):
                
                field_6 = b'aaa'
                
                def method_2(self, param_1):
                    return 2
                
                def method_3(self):
                    ...
                
                @staticmethod
                def static_method_3(param_1):
                    ...
                
                @property
                def property_6(self):
                    return 26
                
                @staticmethod
                def static_method_7(param_1):
                    pass

        expected_contracts = ['field_1', 'property_1', 'class_method_5', 'property_5', 'method_7']
        self.assertContractError(context, expected_contracts)
    
    
    def test_missing_57_2(self):

        self.current_interfaces = self.Interface_5_7
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(*self.current_interfaces):
                
                field_6 = b'aaa'
                
                @property
                def property_1(self):
                    ...
                
                def method_3(self):
                    ...
                
                @property
                def property_5(self):
                    return 5
                
                def method_7(self):
                    ...
        
                @staticmethod
                def static_method_7(param_1):
                    pass

        expected_contracts = ['field_1', 'method_2', 'static_method_3', 'class_method_5', 'property_6']
        self.assertContractError(context, expected_contracts)
    
    
    def test_missing_57_3(self):

        self.current_interfaces = self.Interface_5_7
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(*self.current_interfaces):
                
                field_1 = 1
                
                @property
                def property_1(self):
                    ...
                
                def method_2(self, param_1):
                    return 2
                
                def method_3(self):
                    ...
                
                @property
                def property_5(self):
                    return 5
                
                @staticmethod
                def static_method_7(param_1):
                    pass

        expected_contracts = ['field_6', 'static_method_3', 'class_method_5', 'property_6', 'method_7']
        self.assertContractError(context, expected_contracts)
    

    def test_missing_58_1(self):

        self.current_interfaces = self.Interface_5_8
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(*self.current_interfaces):
                
                field_4 = True
                field_6 = b'aaa'
                field_8 = None
                
                @property
                def property_1(self):
                    ...
                
                def method_2(self, param_1):
                    pass
                
                @staticmethod
                def static_method_3(param_1):
                    ...
                
                @property
                def property_5(self):
                    return 5
                
                def method_7(self):
                    ...
        
                @staticmethod
                def static_method_7(param_1):
                    pass
                
        expected_contracts = ['field_1', 'method_3', 'class_method_5', 'property_6', 'property_8']
        self.assertContractError(context, expected_contracts)
    
    
    def test_missing_58_2(self):

        self.current_interfaces = self.Interface_5_8
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(*self.current_interfaces):
                
                field_1 = 1
                field_6 = b'aaa'
                field_8 = None
                
                @property
                def property_1(self):
                    ...
                
                def method_3(self):
                    return 22
                
                @staticmethod
                def static_method_3(param_1):
                    ...
                
                @property
                def property_5(self):
                    return 5
                
                def method_7(self):
                    ...
        
                @property
                def property_8(self):
                    """Doc`string only"""

        expected_contracts = ['field_4', 'method_2', 'class_method_5', 'property_6', 'static_method_7']
        self.assertContractError(context, expected_contracts)
    
    
    def test_missing_58_3(self):

        self.current_interfaces = self.Interface_5_8
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(*self.current_interfaces):
                
                field_1 = 1
                field_4 = True
                field_6 = b'aaa'
                
                @property
                def property_1(self):
                    ...
                
                def method_2(self, param_1):
                    pass
                
                def method_3(self):
                    return 22
                
                @classmethod
                def class_method_5(cls, a, b):
                    """Docstring only"""
                
                @property
                def property_6(self):
                    return 26
                
                def method_7(self):
                    ...
        
        expected_contracts = ['field_8', 'static_method_3', 'property_5', 'static_method_7', 'property_8']
        self.assertContractError(context, expected_contracts)
    

    def test_missing_49_1(self):

        self.current_interfaces = self.Interface_4_9
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(*self.current_interfaces):
                
                field_1 = 1
                field_6 = b'aaa'
                field_9 = complex(2, 4)
                
                @property
                def property_1(self):
                    return 1
                
                def method_3(self):
                    ...
                
                @staticmethod
                def static_method_3(param_1):
                    ...
                
                @property
                def property_5(self):
                    return 5
                
                def method_9(self):
                    return 99

        expected_contracts = ['field_4', 'method_2', 'class_method_5', 'property_6']
        self.assertContractError(context, expected_contracts)
    
    
    def test_missing_49_2(self):

        self.current_interfaces = self.Interface_4_9
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(*self.current_interfaces):
                
                field_1 = 1
                field_6 = b'aaa'
                field_9 = complex(2, 4)
                
                def method_2(self, param_1):
                    pass
                
                def method_3(self):
                    ...
                
                @classmethod
                def class_method_5(cls, a, b):
                    """Docstring only"""
                
                @property
                def property_5(self):
                    return 5
                
                @property
                def property_6(self):
                    return 26
                
        expected_contracts = ['field_4', 'property_1', 'static_method_3', 'method_9']
        self.assertContractError(context, expected_contracts)
    
    
    def test_missing_49_3(self):

        self.current_interfaces = self.Interface_4_9
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(*self.current_interfaces):
                
                field_1 = 1
                field_4 = True
                field_6 = b'aaa'
                
                def method_2(self, param_1):
                    pass
                
                def method_3(self):
                    ...
                
                @classmethod
                def class_method_5(cls, a, b):
                    """Docstring only"""
                
                @property
                def property_5(self):
                    return 5
                
                def method_9(self):
                    return 99

        expected_contracts = ['field_9', 'property_1', 'static_method_3', 'property_6']
        self.assertContractError(context, expected_contracts)
    

    def test_missing_479_1(self):

        self.current_interfaces = self.Interface_4_7_9
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(*self.current_interfaces):
                
                field_4 = True
                field_6 = b'aaa'
                field_9 = complex(2, 4)
                
                @property
                def property_1(self):
                    ...
                
                def method_3(self):
                    ...
                
                @property
                def property_5(self):
                    return 5
                
                @property
                def property_6(self):
                    return 26
                
                def method_7(self):
                    ...
        
        expected_contracts = ['field_1', 'method_2', 'static_method_3', 'class_method_5', 'static_method_7', 'method_9']
        self.assertContractError(context, expected_contracts)
    
    
    def test_missing_479_2(self):

        self.current_interfaces = self.Interface_4_7_9
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(*self.current_interfaces):
                
                field_1 = 1
                field_4 = True
                field_9 = complex(2, 4)
                
                @property
                def property_1(self):
                    ...
                
                def method_2(self, param_1):
                    pass
                
                def method_3(self):
                    ...
                
                @property
                def property_6(self):
                    return 26
                
                def method_7(self):
                    ...
        
                @staticmethod
                def static_method_7(param_1):
                    pass
                
                def method_9(self):
                    pass

        expected_contracts = ['field_6', 'static_method_3', 'class_method_5', 'property_5']
        self.assertContractError(context, expected_contracts)
    
    
    def test_missing_479_3(self):

        self.current_interfaces = self.Interface_4_7_9
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(*self.current_interfaces):
                
                field_1 = 1
                field_6 = b'aaa'
                
                @property
                def property_1(self):
                    ...
                
                def method_2(self, param_1):
                    pass
                
                def method_3(self):
                    ...
                
                @staticmethod
                def static_method_3(param_1):
                    return param_1
                
                @classmethod
                def class_method_5(cls, a, b):
                    """Docstring only"""
                
                @property
                def property_5(self):
                    return 5
                
                def method_7(self):
                    ...
        
        expected_contracts = ['field_4', 'field_9', 'property_6', 'static_method_7', 'method_9']
        self.assertContractError(context, expected_contracts)


if __name__ == "__main__":
    unittest.main()
