import unittest

import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent.parent.resolve()
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from interface import concrete
from test.concrete.complex_contract.chain.test_helpers import ContractEnforceLeveledTestCase


class ChainedInterfaceMissingLevel4TestCase(ContractEnforceLeveledTestCase):
    
    chain_level = 4
    expected_message_prefix = "Concrete class 'Concrete_4' must implement contracts"

    def test_chain_2_missing_contract_some_1(self):
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete_4(self.Interface_4):
                
                field_2 = "hello"
                field_3 = 5.1
                field_4 = False
                
                def method_1(self):
                    return "Foo"
                
                @classmethod
                def class_method_2(cls):
                    ...
                
                def method_3(self, param_1):
                    pass
                
                @staticmethod
                def static_method_4():
                    pass
                
                @property
                def property_4(self):
                    pass
        
        expected_contracts = ['field_1', 'static_method_2', 'property_3', 'method_4']
        self.assertContractError(context, expected_contracts)
    

    def test_chain_2_missing_contract_some_2(self):
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete_4(self.Interface_4):
                
                field_1 = 2
                field_4 = False
                
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
                
                def method_4(self):
                    pass
                
                @staticmethod
                def static_method_4():
                    pass
                
        expected_contracts = ['field_2', 'field_3', 'class_method_2', 'property_4']
        self.assertContractError(context, expected_contracts)
    

    def test_chain_2_missing_contract_some_3(self):
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete_4(self.Interface_4):
                
                field_1 = 2
                field_2 = "hello"
                field_3 = 5.1
                
                @staticmethod
                def static_method_2(param_1):
                    pass
                
                @classmethod
                def class_method_2(cls):
                    ...
                
                def method_3(self, param_1):
                    pass
                
                def method_4(self):
                    pass
                
                @staticmethod
                def static_method_4():
                    pass
                
                @property
                def property_4(self):
                    pass
        
        expected_contracts = ['field_4', 'property_3', 'method_1']
        self.assertContractError(context, expected_contracts)
    

    def test_chain_2_missing_contract_some_4(self):
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete_4(self.Interface_4):
                
                field_2 = "hello"
                field_4 = False
                
                def method_1(self):
                    return "Foo"
                
                def method_3(self, param_1):
                    pass
                
                @staticmethod
                def static_method_4():
                    pass
                
                @property
                def property_4(self):
                    pass
        
        expected_contracts = ['field_1', 'field_3', 'static_method_2',
                              'class_method_2', 'property_3', 'method_4']
        self.assertContractError(context, expected_contracts)


    def test_chain_2_missing_contract_1_2_all(self):

        with self.assertRaises(TypeError) as context:
            @concrete
            class Concrete_4(self.Interface_4):
                pass
        
        expected_contracts = ['field_1', 'method_1',
                              'field_2', 'static_method_2', 'class_method_2',
                              'field_3', 'method_3', 'property_3',
                              'field_4', 'method_4', 'static_method_4', 'property_4']
        self.assertContractError(context, expected_contracts)


if __name__ == "__main__":
    unittest.main()
