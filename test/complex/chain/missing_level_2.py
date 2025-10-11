import unittest

import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent.resolve()
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from interface import concrete
from test.complex.chain.test_helpers import ContractEnforceLeveledTestCase


class ChainedInterfaceMissingLevel2TestCase(ContractEnforceLeveledTestCase):
    
    chain_level = 2
    expected_message_prefix = "Concrete class 'Concrete_2' must implement contracts"
    
    def test_chain_2_missing_contract_1_field(self):
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete_2(self.Interface_2):
                
                field_2 = "hello"
                
                def method_1(self):
                    return "Foo"
                
                @staticmethod
                def static_method_2(param_1):
                    pass
                
                @classmethod
                def class_method_2(cls):
                    ...
        
        expected_contracts = ['field_1']
        self.assertContractError(context, expected_contracts)

    
    def test_chain_2_missing_contract_1_method(self):

        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete_2(self.Interface_2):
                
                field_1 = 1
                field_2 = "hello"
                
                @staticmethod
                def static_method_2(param_1):
                    pass
                
                @classmethod
                def class_method_2(cls):
                    ...
        
        expected_contracts = ['method_1']
        self.assertContractError(context, expected_contracts)
    
    
    def test_chain_2_missing_contract_2_field(self):

        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete_2(self.Interface_2):
                
                field_1 = 1
                
                def method_1(self):
                    return "Foo"
                
                @staticmethod
                def static_method_2(param_1):
                    pass
                
                @classmethod
                def class_method_2(cls):
                    ...
        
        expected_contracts = ['field_2']
        self.assertContractError(context, expected_contracts)
    
    
    def test_chain_2_missing_contract_2_staticmethod(self):

        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete_2(self.Interface_2):
                
                field_1 = 1
                field_2 = "hello"
                
                def method_1(self):
                    return "Foo"
                
                @classmethod
                def class_method_2(cls):
                    ...
        
        expected_contracts = ['static_method_2']
        self.assertContractError(context, expected_contracts)
        
        
    def test_chain_2_missing_contract_2_classmethod(self):

        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete_2(self.Interface_2):
                
                field_1 = 1
                field_2 = "hello"
                
                def method_1(self):
                    return "Foo"
                
                @staticmethod
                def static_method_2(param_1):
                    pass
                
        expected_contracts = ['class_method_2']
        self.assertContractError(context, expected_contracts)
        
    
    def test_chain_2_missing_contract_1_2_some_1(self):

        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete_2(self.Interface_2):
                
                field_2 = "hello"
                
                def method_1(self):
                    return "Foo"
                
                @classmethod
                def class_method_2(cls):
                    ...
        
        expected_contracts = ['field_1', 'static_method_2']
        self.assertContractError(context, expected_contracts)


    def test_chain_2_missing_contract_1_2_some_2(self):

        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete_2(self.Interface_2):
                
                field_1 = 1
                
                @staticmethod
                def static_method_2(param_1):
                    pass
                
                @classmethod
                def class_method_2(cls):
                    ...
        
        expected_contracts = ['field_2', 'method_1']
        self.assertContractError(context, expected_contracts)


    def test_chain_2_missing_contract_1_2_some_3(self):
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete_2(self.Interface_2):
                
                field_2 = "hello"
                
                def method_1(self):
                    return "Foo"
        
        expected_contracts = ['field_1', 'static_method_2', 'class_method_2']
        self.assertContractError(context, expected_contracts)


    def test_chain_2_missing_contract_1_2_all(self):

        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete_2(self.Interface_2):
                pass
        
        expected_contracts = ['field_1', 'field_2', 'method_1', 'static_method_2', 'class_method_2']
        self.assertContractError(context, expected_contracts)


if __name__ == "__main__":
    unittest.main()
