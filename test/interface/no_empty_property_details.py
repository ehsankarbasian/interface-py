import unittest
from unittest import TestCase

import sys
from pathlib import Path
# find absolute project root
ROOT_PATH = Path(__file__).resolve().parents[2]
if str(ROOT_PATH) not in sys.path:
    sys.path.insert(0, str(ROOT_PATH))

from interface import interface
from test.utils import load_interface_from_source


class InterfaceHasNoPropertyGetterTestCase(TestCase):
    
    def test_no_empty_pass_property_getter(self):
        expected_message = "In interface 'MyInterface', property 'foo' must not define a getter."
        fake_source = '''
            from interface import interface

            @interface
            class MyInterface:
                
                @property
                def foo(self):
                    pass
                
                @foo.getter
                def foo(self):
                    pass
        '''

        with self.assertRaises(TypeError) as context:
            load_interface_from_source(fake_source, "MyInterface")
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_no_empty_ellipsis_property_getter(self):
        expected_message = "In interface 'MyInterface', property 'foo' must not define a getter."
        
        fake_source = '''
            from interface import interface
        
            @interface
            class MyInterface:
                
                @property
                def foo(self):
                    pass
                
                @foo.getter
                def foo(self):
                    ...
        '''
            
        with self.assertRaises(TypeError) as context:
            load_interface_from_source(fake_source, "MyInterface")
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_no_empty_docstring_property_getter(self):
        expected_message = "In interface 'MyInterface', property 'foo' must not define a getter."
        
        fake_source = '''
            from interface import interface
            
            @interface
            class MyInterface:
                
                @property
                def foo(self):
                    pass
                
                @foo.getter
                def foo(self):
                    """ The DocString """
        '''
            
        with self.assertRaises(TypeError) as context:
            load_interface_from_source(fake_source, "MyInterface")
            
        self.assertEqual(str(context.exception), expected_message)


class InterfaceHasNoPropertySetterAndDeleterTestCase(TestCase):
    
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
