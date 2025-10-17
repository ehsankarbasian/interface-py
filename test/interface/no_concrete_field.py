import unittest
from unittest import TestCase

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.absolute())
sys.path.append(path)

from src.interface_py import interface


class InterfaceHasNoConcreteFieldTestCase(TestCase):
    
    def test_no_concrete_field_None(self):
        expected_message = "Attribute 'x' in interface 'MyInterface' should not have a concrete value."
        
        with self.assertRaises(TypeError) as context:
            @interface
            class MyInterface:
                x = None
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_no_concrete_field_NotImplemented(self):
        expected_message = "Attribute 'x' in interface 'MyInterface' should not have a concrete value."
        
        with self.assertRaises(TypeError) as context:
            @interface
            class MyInterface:
                x = NotImplemented
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_no_concrete_field_value_1(self):
        expected_message = "Attribute 'x' in interface 'MyInterface' should not have a concrete value."
        
        with self.assertRaises(TypeError) as context:
            @interface
            class MyInterface:
                x = 3
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_no_concrete_field_value_2(self):
        expected_message = "Attribute 'x' in interface 'MyInterface' should not have a concrete value."
        
        with self.assertRaises(TypeError) as context:
            @interface
            class MyInterface:
                x = 'foo'
            
        self.assertEqual(str(context.exception), expected_message)


if __name__ == "__main__":
    unittest.main()
