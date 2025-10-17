import unittest
from unittest import TestCase

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.parent.absolute())
sys.path.append(path)

from interface_py import interface, concrete


class PropertyContractPassTestCase(TestCase):
    
    def setUp(self):
        
        @interface
        class _MyInterface:
            
            @property
            def foo(self):
                pass
        
        self.MyInterface = _MyInterface
    
    
    def tearDown(self):
        del self.MyInterface
        return super().tearDown()
    
    
    def test_method(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected property, got function."
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                
                def foo(self, par_1, par_2):
                    pass
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_method_bad_params(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected property, got function."
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                
                def foo(par_1, par_bad):
                    pass
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_classmethod(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected property, got classmethod."
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                
                @classmethod
                def foo(self, par_1, par_2):
                    pass
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_classmethod_bad_params(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected property, got classmethod."
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                
                @classmethod
                def foo(par_1, par_bad):
                    pass
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_staticmethod(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected property, got staticmethod."
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                
                @staticmethod
                def foo(self, par_1, par_2):
                    pass
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_staticmethod_bad_params(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected property, got staticmethod."
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                
                @staticmethod
                def foo(par_1, par_bad):
                    pass
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_field(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected property, got field."
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                
                foo = 2
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_field_as_function(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected property, got function."

        def func(self, par_1, par_2):
            pass
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                foo = func
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_field_as_classmethod(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected property, got classmethod."
        
        @classmethod
        def func(cls, par_1, par_2):
            pass
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                foo = func
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_field_as_staticmethod(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected property, got staticmethod."

        @staticmethod
        def func(self, par_1, par_2):
            pass
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                foo = func
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_field_as_property(self):

        @property
        def func(self):
            pass
        
        @concrete
        class MyConcrete(self.MyInterface):
            foo = func


if __name__ == "__main__":
    unittest.main()
