import unittest
from unittest import TestCase

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.absolute())
sys.path.append(path)

from interface import interface


class InterfaceHasNoConcreteLogicTestCase(TestCase):
    
    def test_no_empty_pass_property_getter(self):
        expected_message = "In interface 'MyInterface', property 'foo' must not define a getter."
        
        with self.assertRaises(TypeError) as context:
            
            @interface
            class MyInterface:
                
                @property
                def foo(self):
                    pass
                
                @foo.getter
                def foo(self):
                    pass
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_no_empty_ellipsis_property_getter(self):
        expected_message = "In interface 'MyInterface', property 'foo' must not define a getter."
        
        with self.assertRaises(TypeError) as context:
            
            @interface
            class MyInterface:
                
                @property
                def foo(self):
                    pass
                
                @foo.getter
                def foo(self):
                    ...
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_no_empty_docstring_property_getter(self):
        expected_message = "In interface 'MyInterface', property 'foo' must not define a getter."
        
        with self.assertRaises(TypeError) as context:
            
            @interface
            class MyInterface:
                
                @property
                def foo(self):
                    pass
                
                @foo.getter
                def foo(self):
                    """ The DocString """
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_no_empty_pass_property_setter(self):
        expected_message = "In interface 'MyInterface', property 'foo' must not define a setter."
        
        with self.assertRaises(TypeError) as context:
            
            @interface
            class MyInterface:
                
                @property
                def foo(self):
                    pass
                
                @foo.setter
                def foo(self, value):
                    pass
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_no_empty_ellipsis_property_setter(self):
        expected_message = "In interface 'MyInterface', property 'foo' must not define a setter."
        
        with self.assertRaises(TypeError) as context:
            
            @interface
            class MyInterface:
                
                @property
                def foo(self):
                    pass
                
                @foo.setter
                def foo(self, value):
                    ...
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_no_empty_docstring_property_setter(self):
        expected_message = "In interface 'MyInterface', property 'foo' must not define a setter."
        
        with self.assertRaises(TypeError) as context:
            
            @interface
            class MyInterface:
                
                @property
                def foo(self):
                    pass
                
                @foo.setter
                def foo(self, value):
                    """ The DocString """
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_no_empty_pass_property_deleter(self):
        expected_message = "In interface 'MyInterface', property 'foo' must not define a deleter."
        
        with self.assertRaises(TypeError) as context:
            
            @interface
            class MyInterface:
                
                @property
                def foo(self):
                    pass
                
                @foo.deleter
                def foo(self, value):
                    pass
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_no_empty_ellipsis_property_deleter(self):
        expected_message = "In interface 'MyInterface', property 'foo' must not define a deleter."
        
        with self.assertRaises(TypeError) as context:
            
            @interface
            class MyInterface:
                
                @property
                def foo(self):
                    pass
                
                @foo.deleter
                def foo(self, value):
                    ...
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_no_empty_docstring_property_deleter(self):
        expected_message = "In interface 'MyInterface', property 'foo' must not define a deleter."
        
        with self.assertRaises(TypeError) as context:
            
            @interface
            class MyInterface:
                
                @property
                def foo(self):
                    pass
                
                @foo.deleter
                def foo(self, value):
                    """ The DocString """
            
        self.assertEqual(str(context.exception), expected_message)


if __name__ == "__main__":
    unittest.main()
