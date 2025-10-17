import unittest
from unittest import TestCase

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.parent.absolute())
sys.path.append(path)

from interface_py import interface, concrete


class MethodContractPassTestCase(TestCase):
    
    def setUp(self):
        
        @interface
        class _MyInterface:
            def foo(self, par_1, par_2):
                pass
        
        self.MyInterface = _MyInterface
    
    
    def tearDown(self):
        del self.MyInterface
        return super().tearDown()
    
    
    def test_classmethod(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected function, got classmethod."
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                
                @classmethod
                def foo(self, par_1, par_2):
                    pass
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_classmethod_bad_params(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected function, got classmethod."
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                
                @classmethod
                def foo(cls, par_1):
                    pass
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_staticmethod(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected function, got staticmethod."
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                
                @staticmethod
                def foo(self, par_1, par_2):
                    pass
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_staticmethod_bad_params(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected function, got staticmethod."
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                
                @staticmethod
                def foo(par_1, par_bad):
                    pass
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_field(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected function, got field."
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                
                foo = 2
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_field_as_function(self):
        
        def func(self, par_1, par_2):
            pass
        
        @concrete
        class MyConcrete(self.MyInterface):
            foo = func
    
    
    def test_field_as_classmethod(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected function, got classmethod."

        @classmethod
        def func(self, par_1, par_2):
            pass
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                foo = func
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_field_as_staticmethod(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected function, got staticmethod."

        @staticmethod
        def func(self, par_1, par_2):
            pass
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                foo = func
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_field_as_property(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected function, got property."

        @property
        def func(self):
            pass
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                foo = func
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_property(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected function, got property."
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                
                @property
                def foo(self):
                    pass
            
        self.assertEqual(str(context.exception), expected_message)


if __name__ == "__main__":
    unittest.main()
