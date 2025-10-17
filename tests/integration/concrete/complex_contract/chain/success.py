import unittest

import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent.parent.parent.resolve()
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from interface_py import concrete
from tests.integration.concrete.complex_contract.chain.test_helpers import ContractEnforceTestCase


class ChainedInterfaceSuccessTestCase(ContractEnforceTestCase):

    def test_success_chain_2(self):
        
        @concrete
        class Concrete_2(self.Interface_2):
            
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

        Concrete_2()
    
    
    def test_success_chain_3(self):
        
        @concrete
        class Concrete_3(self.Interface_3):
            
            field_1 = 1
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
            
            @property
            def property_3(self):
                return 'Bar'

        Concrete_3()
    
    
    def test_success_chain_4(self):
        
        @concrete
        class Concrete_4(self.Interface_4):
            
            field_1 = 1
            field_2 = "hello"
            field_3 = None
            field_4 = True
            
            def method_1(self):
                return "Foo"
            
            @staticmethod
            def static_method_2(param_1):
                pass
            
            @classmethod
            def class_method_2(cls):
                """ The DocString """
            
            def method_3(self, param_1):
                ...
            
            @property
            def property_3(self):
                return 'Bar'
            
            def method_4(self):
                pass
            
            @staticmethod
            def static_method_4():
                ...
            
            @property
            def property_4(self):
                ...

        Concrete_4()


if __name__ == "__main__":
    unittest.main()
