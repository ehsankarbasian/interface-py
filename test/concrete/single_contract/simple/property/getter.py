import unittest
from unittest import TestCase

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.parent.parent.parent.absolute())
sys.path.append(path)

from src import interface, concrete


class PropertyGetterContractPassTestCase(TestCase):
    
    def setUp(self):
        
        @interface
        class _MyInterface:
            @property
            def val(self):
                pass
        
        self.MyInterface = _MyInterface
    
    
    def tearDown(self):
        del self.MyInterface
        return super().tearDown()
    
    
    def test_success(self):
        
        @concrete
        class MyConcrete(self.MyInterface):
            
            @property
            def val(self):
                return "The Value"
            
            @val.getter
            def val(self):
                return "Value"
    
    
    def test_instantiate_good_concrete(self):
        
        @concrete
        class MyConcrete(self.MyInterface):
            
            @property
            def val(self):
                return "The Value"
            
            @val.getter
            def val(self):
                return "Value"
        
        MyConcrete()


class PropertyGetterContractEllipsisTestCase(PropertyGetterContractPassTestCase):

    def setUp(self):
        
        @interface
        class _MyInterface:
            @property
            def val(self):
                ...
        
        self.MyInterface = _MyInterface


class PropertyGetterContractDocStringTestCase(PropertyGetterContractPassTestCase):

    def setUp(self):
        
        @interface
        class _MyInterface:
            @property
            def val(self):
                """ The DocString """
        
        self.MyInterface = _MyInterface


if __name__ == "__main__":
    unittest.main()
