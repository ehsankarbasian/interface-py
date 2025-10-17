import unittest
from unittest import TestCase

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.parent.parent.absolute())
sys.path.append(path)

from src.interface_py import interface, concrete


class FieldContractElipsisTestCase(TestCase):
    
    def setUp(self):
        
        @interface
        class _MyInterface:
            x = ...
        
        self.MyInterface = _MyInterface
    
    
    def tearDown(self):
        del self.MyInterface
        return super().tearDown()
    
    
    def test_success(self):
        @concrete
        class MyConcrete(self.MyInterface):
            x = 5
    
    
    def test_instantiate_good_concrete(self):
        @concrete
        class MyConcrete(self.MyInterface):
            x = 5
        
        MyConcrete()
    
    
    def test_no_implement_contract(self):
        expected_message = "Concrete class 'MyConcrete' must implement contracts: x"
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                pass
            
        self.assertEqual(str(context.exception), expected_message)


class FieldContractAnnotationTestCase(FieldContractElipsisTestCase):

    def setUp(self):
        
        @interface
        class _MyInterface:
            x: int

        self.MyInterface = _MyInterface


class FieldContractElipsisAndAnnotationTestCase(FieldContractElipsisTestCase):

    def setUp(self):
        
        @interface
        class _MyInterface:
            x: int = ...

        self.MyInterface = _MyInterface


if __name__ == "__main__":
    unittest.main()
