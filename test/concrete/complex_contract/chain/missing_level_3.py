import unittest

import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent.parent.resolve()
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.interface_py import concrete
from test.concrete.complex_contract.chain.test_helpers import ContractEnforceLeveledTestCase


class ChainedInterfaceMissingLevel3TestCase(ContractEnforceLeveledTestCase):
    
    chain_level = 3
    expected_message_prefix = "Concrete class 'Concrete_3' must implement contracts"

    def test_chain_3_missing_contract_1_field(self):
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete_3(self.Interface_3):
                
                field_2 = "hello"
                field_3 = 2.5
                
                def method_1(self):
                    return "Foo"
                
                @staticmethod
                def static_method_2(param_1):
                    pass
                
                @classmethod
                def class_method_2(cls):
                    ...
                
                def method_3(self, param_1):
                    pass
                
                @property
                def property_3(self):
                    pass
        
        expected_contracts = ['field_1']
        self.assertContractError(context, expected_contracts)

    
    def test_chain_3_missing_contract_1_method(self):

        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete_3(self.Interface_3):
                
                field_1 = 1
                field_2 = "hello"
                field_3 = 2.5
                
                @staticmethod
                def static_method_2(param_1):
                    pass
                
                @classmethod
                def class_method_2(cls):
                    ...
                
                def method_3(self, param_1):
                    pass
                
                @property
                def property_3(self):
                    pass
        
        expected_contracts = ['method_1']
        self.assertContractError(context, expected_contracts)
    
    
    def test_chain_3_missing_contract_2_field(self):

        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete_3(self.Interface_3):
                
                field_1 = 1
                field_3 = 2.5
                
                def method_1(self):
                    return "Foo"
                
                @staticmethod
                def static_method_2(param_1):
                    pass
                
                @classmethod
                def class_method_2(cls):
                    ...
                
                def method_3(self, param_1):
                    pass
                
                @property
                def property_3(self):
                    pass
        
        expected_contracts = ['field_2']
        self.assertContractError(context, expected_contracts)
    
    
    def test_chain_3_missing_contract_2_staticmethod(self):

        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete_3(self.Interface_3):
                
                field_1 = 1
                field_2 = "hello"
                field_3 = 2.5
                
                def method_1(self):
                    return "Foo"
                
                @classmethod
                def class_method_2(cls):
                    ...
                
                def method_3(self, param_1):
                    pass
                
                @property
                def property_3(self):
                    pass
        
        expected_contracts = ['static_method_2']
        self.assertContractError(context, expected_contracts)
        
        
    def test_chain_3_missing_contract_2_classmethod(self):

        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete_3(self.Interface_3):
                
                field_1 = 1
                field_2 = "hello"
                field_3 = 2.5
                
                def method_1(self):
                    return "Foo"
                
                @staticmethod
                def static_method_2(param_1):
                    pass
                
                def method_3(self, param_1):
                    pass
                
                @property
                def property_3(self):
                    pass
                
        expected_contracts = ['class_method_2']
        self.assertContractError(context, expected_contracts)
        
    
    def test_chain_3_missing_contract_3_field(self):

        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete_3(self.Interface_3):
                
                field_1 = 1
                field_2 = "hello"
                
                def method_1(self):
                    return "Foo"
                
                @staticmethod
                def static_method_2(param_1):
                    pass
                
                @classmethod
                def class_method_2(cls):
                    ...
                
                def method_3(self, param_1):
                    pass
                
                @property
                def property_3(self):
                    pass
        
        expected_contracts = ['field_3']
        self.assertContractError(context, expected_contracts)
        
        
    def test_chain_3_missing_contract_3_method(self):
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete_3(self.Interface_3):
                
                field_1 = 1
                field_2 = "hello"
                field_3 = 2.5
                
                def method_1(self):
                    return "Foo"
                
                @staticmethod
                def static_method_2(param_1):
                    pass
                
                @classmethod
                def class_method_2(cls):
                    ...
                
                @property
                def property_3(self):
                    pass
        
        expected_contracts = ['method_3']
        self.assertContractError(context, expected_contracts)
        
    
    def test_chain_3_missing_contract_3_property(self):

        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete_3(self.Interface_3):
                
                field_1 = 1
                field_2 = "hello"
                field_3 = 2.5
                
                def method_1(self):
                    return "Foo"
                
                @staticmethod
                def static_method_2(param_1):
                    pass
                
                @classmethod
                def class_method_2(cls):
                    ...
                
                def method_3(self, param_1):
                    pass
                
        expected_contracts = ['property_3']
        self.assertContractError(context, expected_contracts)
    
    
    def test_chain_3_missing_contract_1_2_some_1(self):

        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete_3(self.Interface_3):
                
                field_2 = "hello"
                field_3 = 2.5
                
                def method_1(self):
                    return "Foo"
                
                @classmethod
                def class_method_2(cls):
                    ...
                
                def method_3(self, param_1):
                    pass
                
                @property
                def property_3(self):
                    pass
        
        expected_contracts = ['field_1', 'static_method_2']
        self.assertContractError(context, expected_contracts)


    def test_chain_3_missing_contract_1_2_some_2(self):

        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete_3(self.Interface_3):
                
                field_1 = 1
                field_3 = 2.5
                
                @staticmethod
                def static_method_2(param_1):
                    pass
                
                @classmethod
                def class_method_2(cls):
                    ...
                
                def method_3(self, param_1):
                    pass
                
                @property
                def property_3(self):
                    pass
        
        expected_contracts = ['field_2', 'method_1']
        self.assertContractError(context, expected_contracts)


    def test_chain_3_missing_contract_1_2_some_3(self):
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete_3(self.Interface_3):
                
                field_2 = "hello"
                field_3 = 2.5
                
                def method_1(self):
                    return "Foo"
                
                def method_3(self, param_1):
                    pass
                
                @property
                def property_3(self):
                    pass
        
        expected_contracts = ['field_1', 'static_method_2', 'class_method_2']
        self.assertContractError(context, expected_contracts)
    
    
    def test_chain_3_missing_contract_1_3_some_1(self):

        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete_3(self.Interface_3):
                
                field_2 = "hello"
                field_3 = None
                
                def method_1(self):
                    return "Foo"
                
                @staticmethod
                def static_method_2(param_1):
                    pass
                
                @classmethod
                def class_method_2(cls):
                    """ The DocString """
                
                def method_3(self, param_1):
                    pass
                
        expected_contracts = ['field_1', 'property_3']
        self.assertContractError(context, expected_contracts)
    

    def test_chain_3_missing_contract_1_3_some_2(self):

        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete_3(self.Interface_3):
                
                field_1 = 1
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
                
        expected_contracts = ['method_1', 'method_3']
        self.assertContractError(context, expected_contracts)
    

    def test_chain_3_missing_contract_1_3_some_3(self):

        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete_3(self.Interface_3):
                
                field_1 = 1
                field_2 = "hello"
                
                @staticmethod
                def static_method_2(param_1):
                    pass
                
                @classmethod
                def class_method_2(cls):
                    """ The DocString """
                
                def method_3(self, param_1):
                    pass
                
        expected_contracts = ['method_1', 'field_3', 'property_3']
        self.assertContractError(context, expected_contracts)
    

    def test_chain_3_missing_contract_2_3_some_1(self):

        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete_3(self.Interface_3):
                
                field_1 = 1
                field_2 = "hello"
                field_3 = None
                
                def method_1(self):
                    return "Foo"
                
                @classmethod
                def class_method_2(cls):
                    """ The DocString """
                
                @property
                def property_3(self):
                    return 'Bar'
                
        expected_contracts = ['static_method_2', 'method_3']
        self.assertContractError(context, expected_contracts)
    

    def test_chain_3_missing_contract_2_3_some_2(self):

        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete_3(self.Interface_3):
                
                field_1 = 1
                field_3 = None
                
                def method_1(self):
                    return "Foo"
                
                @staticmethod
                def static_method_2(param_1):
                    pass
                
                @classmethod
                def class_method_2(cls):
                    """ The DocString """
                
                def method_3(self, param_1):
                    pass
                
        expected_contracts = ['field_2', 'property_3']
        self.assertContractError(context, expected_contracts)
    

    def test_chain_3_missing_contract_2_3_some_3(self):

        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete_3(self.Interface_3):
                
                field_1 = 1
                field_2 = "hello"
                
                def method_1(self):
                    return "Foo"
                
                @staticmethod
                def static_method_2(param_1):
                    pass
                
                def method_3(self, param_1):
                    pass
                
        expected_contracts = ['class_method_2', 'field_3', 'property_3']
        self.assertContractError(context, expected_contracts)
    
    
    def test_chain_3_missing_contract_1_2_3_some_1(self):

        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete_3(self.Interface_3):
                
                field_2 = "hello"
                
                def method_1(self):
                    return "Foo"
                
                @classmethod
                def class_method_2(cls):
                    """ The DocString """
                
                def method_3(self, param_1):
                    pass
                
        expected_contracts = ['field_1', 'static_method_2', 'field_3', 'property_3']
        self.assertContractError(context, expected_contracts)
    
    
    def test_chain_3_missing_contract_1_2_3_some_2(self):

        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete_3(self.Interface_3):
                
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
                
        expected_contracts = ['method_1', 'field_2', 'method_3']
        self.assertContractError(context, expected_contracts)
    
    
    def test_chain_3_missing_contract_1_2_3_some_3(self):

        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete_3(self.Interface_3):
                
                field_2 = "hello"
                field_3 = None
                
                def method_1(self):
                    return "Foo"
                
                @staticmethod
                def static_method_2(param_1):
                    pass
                
        expected_contracts = ['field_1', 'class_method_2', 'property_3', 'method_3']
        self.assertContractError(context, expected_contracts)


    def test_chain_3_missing_contract_1_2_3_all(self):

        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete_3(self.Interface_3):
                pass
        
        expected_contracts = ['field_1', 'method_1',
                              'field_2', 'static_method_2', 'class_method_2',
                              'field_3', 'method_3', 'property_3']
        self.assertContractError(context, expected_contracts)
    

if __name__ == "__main__":
    unittest.main()
