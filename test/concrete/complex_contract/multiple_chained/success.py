import unittest

import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent.parent.resolve()
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src import concrete
from test.concrete.complex_contract.multiple_chained.test_helpers import ContractEnforceTestCase


class MultipleInterfaceSuccessTestCase(ContractEnforceTestCase):
    

    def test_success_2_4(self):
        self.current_interfaces = self.Interface_2_4
        
        @concrete
        class Concrete(*self.current_interfaces):
            
            field_1 = 1
            field_4 = None
            
            @property
            def property_1(self):
                return 26
            
            def method_2(self, param_1):
                pass
            
            def method_3(self):
                ...
            
            @staticmethod
            def static_method_3(param_1):
                ...
        
        Concrete()
    
    
    def test_success_2_4_7(self):
        
        self.current_interfaces = self.Interface_2_4_7
        
        @concrete
        class Concrete(*self.current_interfaces):
            
            field_1 = None
            field_4 = True
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
                ...
            
            @property
            def property_6(self):
                return 26
            
            def method_7(self):
                ...
    
            @staticmethod
            def static_method_7(param_1):
                pass
        
        Concrete()
    
    
    def test_success_5_7(self):

        self.current_interfaces = self.Interface_5_7
        
        @concrete
        class Concrete(*self.current_interfaces):
            
            field_1 = 1
            field_6 = b'aaa'
            
            @property
            def property_1(self):
                ...
            
            def method_2(self, param_1):
                return 2
            
            def method_3(self):
                ...
            
            @staticmethod
            def static_method_3(param_1):
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
            
            def method_7(self):
                ...
    
            @staticmethod
            def static_method_7(param_1):
                pass

        Concrete()
    

    def test_success_5_8(self):

        self.current_interfaces = self.Interface_5_8
        
        @concrete
        class Concrete(*self.current_interfaces):
            
            field_1 = 1
            field_4 = True
            field_6 = b'aaa'
            field_8 = None
            
            @property
            def property_1(self):
                ...
            
            def method_2(self, param_1):
                pass
            
            def method_3(self):
                return 22
            
            @staticmethod
            def static_method_3(param_1):
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
            
            def method_7(self):
                ...
    
            @staticmethod
            def static_method_7(param_1):
                pass
            
            @property
            def property_8(self):
                """Docstring only"""

        Concrete()
    

    def test_success_4_9(self):

        self.current_interfaces = self.Interface_4_9
        
        @concrete
        class Concrete(*self.current_interfaces):
            
            field_1 = 1
            field_4 = True
            field_6 = b'aaa'
            field_9 = complex(2, 4)
            
            @property
            def property_1(self):
                return 1
            
            def method_2(self, param_1):
                pass
            
            def method_3(self):
                ...
            
            @staticmethod
            def static_method_3(param_1):
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
            
            def method_9(self):
                return 99

        Concrete()
    

    def test_success_4_7_9(self):

        self.current_interfaces = self.Interface_4_7_9
        
        @concrete
        class Concrete(*self.current_interfaces):
            
            field_1 = 1
            field_4 = True
            field_6 = b'aaa'
            field_9 = complex(2, 4)
            
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

        Concrete()


if __name__ == "__main__":
    unittest.main()
