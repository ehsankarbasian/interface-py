import unittest

import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent.parent.resolve()
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from interface import concrete
from test.concrete.complex_contract.multiple.test_helpers import ContractEnforceTestCase


class MultipleInterfaceSuccessTestCase(ContractEnforceTestCase):
    
    def test_success_1_2(self):
        
        @concrete
        class Concrete(self.Interface_1, self.Interface_2):
            
            field_1 = 1
            field_2 = "hello"
            
            def method_1(self):
                return "Foo"
            
            @staticmethod
            def static_method_2(param_1):
                pass
            
            @classmethod
            def class_method_2(cls):
                """ The DocString """
        
        Concrete()
    
    
    def test_success_1_3(self):
        
        @concrete
        class Concrete(self.Interface_1, self.Interface_3):
            
            field_1 = 1
            field_3 = None
            
            def method_1(self):
                return "Foo"
            
            def method_3(self, param_1):
                ...
            
            @property
            def property_3(self):
                return 'Bar'
        
        Concrete()


    def test_success_1_4(self):
        
        @concrete
        class Concrete(self.Interface_1, self.Interface_4):
            
            field_1 = 1
            field_4 = True
            
            def method_1(self):
                return "Foo"
            
            def method_4(self):
                pass
            
            @staticmethod
            def static_method_4():
                ...
            
            @property
            def property_4(self):
                ...
        
        Concrete()


    def test_success_2_3(self):
        
        @concrete
        class Concrete(self.Interface_2, self.Interface_3):
            
            field_2 = "hello"
            field_3 = None
            
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
        
        Concrete()


    def test_success_2_4(self):
        
        @concrete
        class Concrete(self.Interface_2, self.Interface_4):
            
            field_2 = "hello"
            field_4 = True
            
            @staticmethod
            def static_method_2(param_1):
                pass
            
            @classmethod
            def class_method_2(cls):
                """ The DocString """
            
            def method_4(self):
                pass
            
            @staticmethod
            def static_method_4():
                ...
            
            @property
            def property_4(self):
                ...
        
        Concrete()


    def test_success_3_4(self):
        
        @concrete
        class Concrete(self.Interface_3, self.Interface_4):
            
            field_3 = None
            field_4 = True
            
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
        
        Concrete()


    def test_success_1_2_3(self):
        
        @concrete
        class Concrete(self.Interface_1, self.Interface_2, self.Interface_3):
            
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
                ...
            
            @property
            def property_3(self):
                return 'Bar'
        
        Concrete()


    def test_success_1_2_4(self):
        
        @concrete
        class Concrete(self.Interface_1, self.Interface_2, self.Interface_4):
            
            field_1 = 1
            field_2 = "hello"
            field_4 = True
            
            def method_1(self):
                return "Foo"
            
            @staticmethod
            def static_method_2(param_1):
                pass
            
            @classmethod
            def class_method_2(cls):
                """ The DocString """
            
            def method_4(self):
                pass
            
            @staticmethod
            def static_method_4():
                ...
            
            @property
            def property_4(self):
                ...
        
        Concrete()


    def test_success_1_3_4(self):
        
        @concrete
        class Concrete(self.Interface_1, self.Interface_3, self.Interface_4):
            
            field_1 = 1
            field_3 = None
            field_4 = True
            
            def method_1(self):
                return "Foo"
            
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
        
        Concrete()
    
    
    def test_success_2_3_4(self):
        
        @concrete
        class Concrete(self.Interface_2, self.Interface_3, self.Interface_4):
            
            field_2 = "hello"
            field_3 = None
            field_4 = True
            
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
    
    
    def test_success_1_2_3_4(self):
        
        @concrete
        class Concrete(self.Interface_1, self.Interface_2, self.Interface_3, self.Interface_4):
            
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


if __name__ == "__main__":
    unittest.main()
