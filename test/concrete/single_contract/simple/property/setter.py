import unittest
from unittest import TestCase

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.parent.parent.parent.absolute())
sys.path.append(path)

from src import interface, concrete


class PropertySetterContractPassTestCase(TestCase):
    
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
            
            @val.setter
            def val(self, value):
                self.t = value
    
    
    def test_instantiate_good_concrete(self):
        @concrete
        class MyConcrete(self.MyInterface):
            
            @property
            def val(self):
                return "The Value"
            
            @val.setter
            def val(self, value):
                self.t = value
        
        MyConcrete()
    
    
    def test_setter_works(self):
        @concrete
        class MyConcrete(self.MyInterface):
            
            @property
            def val(self):
                return "The Value"
            
            @val.setter
            def val(self, value):
                self.t = value
        
        instance = MyConcrete()
        instance.val = 'NEW'
        self.assertEqual(instance.t, 'NEW')


class PropertySetterContractEllipsisTestCase(PropertySetterContractPassTestCase):

    def setUp(self):
        
        @interface
        class _MyInterface:
            
            @property
            def val(self):
                ...
        
        self.MyInterface = _MyInterface


class PropertySetterContractDocStringTestCase(PropertySetterContractPassTestCase):

    def setUp(self):
        
        @interface
        class _MyInterface:
            
            @property
            def val(self):
                """ The DocString """
        
        self.MyInterface = _MyInterface


if __name__ == "__main__":
    unittest.main()
