import unittest
from unittest import TestCase

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.parent.parent.absolute())
sys.path.append(path)

from interface import interface, concrete


class PropertyContractPassTestCase(TestCase):
    
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
    
    
    def test_instantiate_good_concrete(self):
        @concrete
        class MyConcrete(self.MyInterface):
            @property
            def val(self):
                return "The Value"
        
        MyConcrete()
    
    
    def test_no_implement_contract(self):
        expected_message = "Concrete class 'MyConcrete' must implement contracts: val"
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                pass
            
        self.assertEqual(str(context.exception), expected_message)


class PropertyContractEllipsisTestCase(PropertyContractPassTestCase):

    def setUp(self):
        
        @interface
        class _MyInterface:
            @property
            def val(self):
                ...
        
        self.MyInterface = _MyInterface


class PropertyContractDocStringTestCase(PropertyContractPassTestCase):

    def setUp(self):
        
        @interface
        class _MyInterface:
            @property
            def val(self):
                """ The DocString """
        
        self.MyInterface = _MyInterface


if __name__ == "__main__":
    unittest.main()
