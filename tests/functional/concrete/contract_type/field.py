import unittest
from unittest import TestCase

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.parent.absolute())
sys.path.append(path)

from interface_py import interface, concrete


class FieldContractTypeTestCase(TestCase):
    
    def setUp(self):
        
        @interface
        class _MyInterface:
            x = ...
        
        self.MyInterface = _MyInterface
    
    
    def tearDown(self):
        del self.MyInterface
        return super().tearDown()
    
    
    def test_field_as_function(self):
        expected_message = "Contract violation for 'x' in 'MyConcrete': expected a field, got function."
        
        def func(self, par_1, par_2):
            pass
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                x = func
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_field_as_classmethod(self):
        expected_message = "Contract violation for 'x' in 'MyConcrete': expected a field, got classmethod."
        
        @classmethod
        def func(self, par_1, par_2):
            pass
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                x = func
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_field_as_staticmethod(self):
        expected_message = "Contract violation for 'x' in 'MyConcrete': expected a field, got staticmethod."

        @staticmethod
        def func(self, par_1, par_2):
            pass
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                x = func
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_field_as_property(self):
        expected_message = "Contract violation for 'x' in 'MyConcrete': expected a field, got property."

        @property
        def func(self):
            pass
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                x = func
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_method(self):
        expected_message = "Contract violation for 'x' in 'MyConcrete': expected a field, got function."
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                
                def x(self):
                    return
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_classmethod(self):
        expected_message = "Contract violation for 'x' in 'MyConcrete': expected a field, got classmethod."
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                
                @classmethod
                def x(cls): 
                    return
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_staticmethod(self):
        expected_message = "Contract violation for 'x' in 'MyConcrete': expected a field, got staticmethod."
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                
                @staticmethod
                def x(self):
                    return
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_property(self):
        expected_message = "Contract violation for 'x' in 'MyConcrete': expected a field, got property."
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                
                @property
                def x(self):
                    return
            
        self.assertEqual(str(context.exception), expected_message)


if __name__ == "__main__":
    unittest.main()
