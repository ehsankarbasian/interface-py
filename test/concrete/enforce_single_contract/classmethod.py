import unittest
from unittest import TestCase

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.parent.absolute())
sys.path.append(path)

from interface import interface, concrete


class ClassMethodContractTestCase(TestCase):
    
    def setUp(self):
        
        @interface
        class _MyInterface:
            @classmethod
            def foo(cls, par_1, par_2):
                pass
        
        self.MyInterface = _MyInterface
    
    
    def tearDown(self):
        del self.MyInterface
        return super().tearDown()
    
    
    def test_success(self):
        @concrete
        class MyConcrete(self.MyInterface):
            @classmethod
            def foo(cls, par_1, par_2):
                return f'{par_1} {par_2}'
    
    
    def test_instantiate_good_concrete(self):
        @concrete
        class MyConcrete(self.MyInterface):
            @classmethod
            def foo(cls, par_1, par_2):
                return f'{par_1} {par_2}'
        
        MyConcrete()
    
    
    def test_not_the_same_params(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected (cls, par_1, par_2), got (cls, par_1)."
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                @classmethod
                def foo(cls, par_1):
                    return par_1
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_no_implement_contract(self):
        expected_message = "Concrete class 'MyConcrete' must implement contracts: foo"
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                pass
            
        self.assertEqual(str(context.exception), expected_message)


if __name__ == "__main__":
    unittest.main()
