import unittest

import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent.parent.resolve()
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from interface_py import concrete
from test.concrete.complex_contract.multiple.test_helpers import ContractEnforceMultipleTestCase


class MultipleInterfaceMissingTestCase(ContractEnforceMultipleTestCase):
    
    expected_message_prefix = "Concrete class 'Concrete' must implement contracts"
    
    
    def test_missing_12_1(self):

        self.current_interfaces = [1, 2]
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(self.Interface_1, self.Interface_2):
                
                field_1 = 1
                field_2 = "hello"
                
                @staticmethod
                def static_method_2(param_1):
                    pass
                
        expected_contracts = ['method_1', 'class_method_2']
        self.assertContractError(context, expected_contracts)
    

    def test_missing_12_2(self):

        self.current_interfaces = [1, 2]
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(self.Interface_1, self.Interface_2):
                
                field_2 = "hello"
                
                @staticmethod
                def static_method_2(param_1):
                    pass
                
        expected_contracts = ['field_1', 'method_1', 'class_method_2']
        self.assertContractError(context, expected_contracts)
    

    def test_missing_12_3(self):

        self.current_interfaces = [1, 2]
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(self.Interface_1, self.Interface_2):
                
                def method_1(self):
                    return "Foo"
                
        expected_contracts = ['field_1', 'field_2', 'static_method_2', 'class_method_2']
        self.assertContractError(context, expected_contracts)
    

    def test_missing_13_1(self):

        self.current_interfaces = [1, 3]
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(self.Interface_1, self.Interface_3):
                
                field_1 = 1
                field_3 = None
                
        expected_contracts = ['method_1', 'method_3', 'property_3']
        self.assertContractError(context, expected_contracts)
    

    def test_missing_13_2(self):

        self.current_interfaces = [1, 3]
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(self.Interface_1, self.Interface_3):
                
                field_1 = 1
                
                def method_1(self):
                    return "Foo"
                
                def method_3(self, param_1):
                    ...
                
        expected_contracts = ['field_3', 'property_3']
        self.assertContractError(context, expected_contracts)
    

    def test_missing_13_3(self):

        self.current_interfaces = [1, 3]
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(self.Interface_1, self.Interface_3):
                
                field_3 = None
                
                @property
                def property_3(self):
                    return 'Bar'
        
        expected_contracts = ['field_1', 'method_1', 'method_3']
        self.assertContractError(context, expected_contracts)
    

    def test_missing_14_1(self):

        self.current_interfaces = [1, 4]
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(self.Interface_1, self.Interface_4):
                
                def method_1(self):
                    return "Foo"
                
                @property
                def property_4(self):
                    ...
        
        expected_contracts = ['field_1', 'field_4', 'method_4', 'static_method_4']
        self.assertContractError(context, expected_contracts)
    

    def test_missing_14_2(self):

        self.current_interfaces = [1, 4]
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(self.Interface_1, self.Interface_4):
                
                field_1 = 1
                
                def method_4(self):
                    pass
                
                @staticmethod
                def static_method_4():
                    ...
                
        expected_contracts = ['field_4', 'method_1', 'property_4']
        self.assertContractError(context, expected_contracts)
    

    def test_missing_14_3(self):

        self.current_interfaces = [1, 4]
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(self.Interface_1, self.Interface_4):
                
                field_4 = True
                
                def method_1(self):
                    return "Foo"
                
                @staticmethod
                def static_method_4():
                    ...
                
        expected_contracts = ['field_1', 'method_4', 'property_4']
        self.assertContractError(context, expected_contracts)
    

    def test_missing_23_1(self):

        self.current_interfaces = [2, 3]
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(self.Interface_2, self.Interface_3):
                
                field_2 = "hello"
                field_3 = None
                
                @classmethod
                def class_method_2(cls):
                    """ The DocString """
                
                @property
                def property_3(self):
                    return 'Bar'
                
        expected_contracts = ['static_method_2', 'method_3']
        self.assertContractError(context, expected_contracts)
    

    def test_missing_23_2(self):

        self.current_interfaces = [2, 3]
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(self.Interface_2, self.Interface_3):
                
                @classmethod
                def class_method_2(cls):
                    """ The DocString """
                
                def method_3(self, param_1):
                    ...
                
        expected_contracts = ['field_2', 'field_3', 'static_method_2', 'property_3']
        self.assertContractError(context, expected_contracts)
    

    def test_missing_23_3(self):

        self.current_interfaces = [2, 3]
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(self.Interface_2, self.Interface_3):
                
                field_3 = None
                
                def method_3(self, param_1):
                    ...
                
        expected_contracts = ['field_2', 'static_method_2', 'class_method_2', 'property_3']
        self.assertContractError(context, expected_contracts)
    

    def test_missing_24_1(self):

        self.current_interfaces = [2, 4]
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(self.Interface_2, self.Interface_4):
                
                field_2 = "hello"
                field_4 = True
                
                @classmethod
                def class_method_2(cls):
                    """ The DocString """
                
                @staticmethod
                def static_method_4():
                    ...
                
                @property
                def property_4(self):
                    ...
        
        expected_contracts = ['static_method_2', 'method_4']
        self.assertContractError(context, expected_contracts)
    

    def test_missing_24_2(self):

        self.current_interfaces = [2, 4]
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(self.Interface_2, self.Interface_4):
                
                field_2 = "hello"
                
                @staticmethod
                def static_method_2(param_1):
                    pass
                
                @property
                def property_4(self):
                    ...
        
        expected_contracts = ['field_4', 'class_method_2', 'method_4', 'static_method_4']
        self.assertContractError(context, expected_contracts)
    

    def test_missing_24_3(self):

        self.current_interfaces = [2, 4]
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(self.Interface_2, self.Interface_4):
                
                field_4 = True
                
                @classmethod
                def class_method_2(cls):
                    """ The DocString """
                
                @staticmethod
                def static_method_4():
                    ...
                
        expected_contracts = ['field_2', 'static_method_2', 'method_4', 'property_4']
        self.assertContractError(context, expected_contracts)
    

    def test_missing_34_1(self):

        self.current_interfaces = [3, 4]
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(self.Interface_3, self.Interface_4):
                
                field_3 = None
                field_4 = True
                
                def method_4(self):
                    pass
                
                @property
                def property_4(self):
                    ...
        
        expected_contracts = ['method_3', 'property_3', 'static_method_4']
        self.assertContractError(context, expected_contracts)
    

    def test_missing_34_2(self):

        self.current_interfaces = [3, 4]
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(self.Interface_3, self.Interface_4):
                
                field_4 = True
                
                def method_3(self, param_1):
                    ...
                
                @staticmethod
                def static_method_4():
                    ...
                
                @property
                def property_4(self):
                    ...
        
        expected_contracts = ['field_3', 'property_3', 'method_4']
        self.assertContractError(context, expected_contracts)
    

    def test_missing_34_3(self):

        self.current_interfaces = [3, 4]
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(self.Interface_3, self.Interface_4):
                
                field_4 = True
                
                @property
                def property_3(self):
                    return 'Bar'
                
                def method_4(self):
                    pass
                
        expected_contracts = ['field_3', 'method_3', 'static_method_4', 'property_4']
        self.assertContractError(context, expected_contracts)
    
    
    def test_missing_123_1(self):

        self.current_interfaces = [1, 2, 3]
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(self.Interface_1, self.Interface_2, self.Interface_3):
                
                field_1 = 1
                field_3 = None
                
                @staticmethod
                def static_method_2(param_1):
                    pass
                
                @classmethod
                def class_method_2(cls):
                    """ The DocString """
                
                @property
                def property_3(self):
                    return 'Bar'
                
        expected_contracts = ['field_2', 'method_1', 'method_3']
        self.assertContractError(context, expected_contracts)
    

    def test_missing_123_2(self):

        self.current_interfaces = [1, 2, 3]
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(self.Interface_1, self.Interface_2, self.Interface_3):
                
                field_1 = 1
                
                @staticmethod
                def static_method_2(param_1):
                    pass
                
                @classmethod
                def class_method_2(cls):
                    """ The DocString """
                
                def method_3(self, param_1):
                    ...
                
        expected_contracts = ['field_2', 'field_3', 'method_1', 'property_3']
        self.assertContractError(context, expected_contracts)
    

    def test_missing_123_3(self):

        self.current_interfaces = [1, 2, 3]
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(self.Interface_1, self.Interface_2, self.Interface_3):
                
                field_2 = "hello"
                field_3 = None
                
                @classmethod
                def class_method_2(cls):
                    """ The DocString """
                
                def method_3(self, param_1):
                    ...
                
        expected_contracts = ['field_1', 'method_1', 'static_method_2', 'property_3']
        self.assertContractError(context, expected_contracts)
    

    def test_missing_124_1(self):

        self.current_interfaces = [1, 2, 4]
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(self.Interface_1, self.Interface_2, self.Interface_4):
                
                field_1 = 1
                
                @staticmethod
                def static_method_2(param_1):
                    pass
                
                def method_4(self):
                    pass
                
                @staticmethod
                def static_method_4():
                    ...
                
                @property
                def property_4(self):
                    ...
        
        expected_contracts = ['field_2', 'field_4', 'method_1', 'class_method_2']
        self.assertContractError(context, expected_contracts)
    

    def test_missing_124_2(self):

        self.current_interfaces = [1, 2, 4]
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(self.Interface_1, self.Interface_2, self.Interface_4):
                
                field_1 = 1
                field_2 = "hello"
                
                def method_1(self):
                    return "Foo"
                
                @staticmethod
                def static_method_2(param_1):
                    pass
                
                @property
                def property_4(self):
                    ...
        
        expected_contracts = ['field_4', 'class_method_2', 'method_4', 'static_method_4']
        self.assertContractError(context, expected_contracts)
    

    def test_missing_124_3(self):

        self.current_interfaces = [1, 2, 4]
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(self.Interface_1, self.Interface_2, self.Interface_4):
                
                field_2 = "hello"
                field_4 = True
                
                @classmethod
                def class_method_2(cls):
                    """ The DocString """
                
                @staticmethod
                def static_method_4():
                    ...
                
                @property
                def property_4(self):
                    ...
        
        expected_contracts = ['field_1', 'method_1', 'static_method_2', 'method_4']
        self.assertContractError(context, expected_contracts)
    

    def test_missing_234_1(self):

        self.current_interfaces = [2, 3, 4]
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(self.Interface_2, self.Interface_3, self.Interface_4):
                
                field_2 = "hello"
                field_3 = None
                
                @staticmethod
                def static_method_2(param_1):
                    pass
                
                @classmethod
                def class_method_2(cls):
                    """ The DocString """
                
                @property
                def property_3(self):
                    return 'Bar'
                
                @staticmethod
                def static_method_4():
                    ...
                
        expected_contracts = ['field_4', 'method_3', 'method_4', 'property_4']
        self.assertContractError(context, expected_contracts)
    

    def test_missing_234_2(self):

        self.current_interfaces = [2, 3, 4]
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(self.Interface_2, self.Interface_3, self.Interface_4):
                
                field_2 = "hello"
                field_4 = True
                
                @classmethod
                def class_method_2(cls):
                    """ The DocString """
                
                @property
                def property_3(self):
                    return 'Bar'
                
                def method_4(self):
                    pass
                
                @property
                def property_4(self):
                    ...
        
        expected_contracts = ['field_3', 'static_method_2', 'method_3', 'static_method_4']
        self.assertContractError(context, expected_contracts)
    

    def test_missing_234_3(self):

        self.current_interfaces = [2, 3, 4]
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(self.Interface_2, self.Interface_3, self.Interface_4):
                
                field_3 = None
                
                @staticmethod
                def static_method_2(param_1):
                    pass
                
                @classmethod
                def class_method_2(cls):
                    """ The DocString """
                
                def method_3(self, param_1):
                    ...
                
                def method_4(self):
                    pass
                
                @property
                def property_4(self):
                    ...
        
        expected_contracts = ['field_2', 'field_4', 'static_method_4', 'property_3']
        self.assertContractError(context, expected_contracts)
        
        
    def test_missing_1234_1(self):

        self.current_interfaces = [1, 2, 3, 4]
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(self.Interface_1, self.Interface_2, self.Interface_3, self.Interface_4):
                
                field_2 = "hello"
                field_3 = None
                field_4 = True
                
                def method_1(self):
                    return "Foo"
                
                @classmethod
                def class_method_2(cls):
                    """ The DocString """
                
                def method_3(self, param_1):
                    ...
                
                @staticmethod
                def static_method_4():
                    ...
                
                @property
                def property_4(self):
                    ...
        
        expected_contracts = ['field_1', 'static_method_2', 'property_3', 'method_4']
        self.assertContractError(context, expected_contracts)
    

    def test_missing_1234_2(self):

        self.current_interfaces = [1, 2, 3, 4]
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(self.Interface_1, self.Interface_2, self.Interface_3, self.Interface_4):
                
                field_1 = 1
                field_3 = None
                
                @staticmethod
                def static_method_2(param_1):
                    pass
                
                @classmethod
                def class_method_2(cls):
                    """ The DocString """
                
                @property
                def property_3(self):
                    return 'Bar'
                
                def method_4(self):
                    pass
                
                @staticmethod
                def static_method_4():
                    ...
                
        expected_contracts = ['method_1', 'field_2', 'field_4', 'method_3', 'property_4']
        self.assertContractError(context, expected_contracts)
    

    def test_missing_1234_3(self):

        self.current_interfaces = [1, 2, 3, 4]
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(self.Interface_1, self.Interface_2, self.Interface_3, self.Interface_4):
                
                field_1 = 1
                field_2 = "hello"
                field_3 = None
                field_4 = True
                
                def method_1(self):
                    return "Foo"
                
                @classmethod
                def class_method_2(cls):
                    """ The DocString """
                
                def method_3(self, param_1):
                    ...
                
                def method_4(self):
                    pass
                
        
        expected_contracts = ['static_method_2', 'property_3', 'static_method_4', 'property_4']
        self.assertContractError(context, expected_contracts)
    

    def test_missing_1234_4(self):

        self.current_interfaces = [1, 2, 3, 4]
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(self.Interface_1, self.Interface_2, self.Interface_3, self.Interface_4):
                
                field_2 = "hello"
                field_3 = None
                field_4 = True
                
                def method_1(self):
                    return "Foo"
                
                @staticmethod
                def static_method_2(param_1):
                    pass
                
                @property
                def property_3(self):
                    return 'Bar'
                
                def method_4(self):
                    pass
                
                @property
                def property_4(self):
                    ...
        
        expected_contracts = ['field_1', 'class_method_2', 'method_3', 'static_method_4']
        self.assertContractError(context, expected_contracts)
    

    def test_missing_1234_5(self):
        
        self.current_interfaces = [1, 2, 3, 4]
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete(self.Interface_1, self.Interface_2, self.Interface_3, self.Interface_4):
                
                field_2 = "hello"
                
                def method_1(self):
                    return "Foo"
                
                @classmethod
                def class_method_2(cls):
                    """ The DocString """
                
                def method_3(self, param_1):
                    ...
                
                def method_4(self):
                    pass
                
                @property
                def property_4(self):
                    ...
        
        expected_contracts = ['field_1', 'field_3', 'field_4', 'static_method_2', 'property_3', 'static_method_4']
        self.assertContractError(context, expected_contracts)


if __name__ == "__main__":
    unittest.main()
