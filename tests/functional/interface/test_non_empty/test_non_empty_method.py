import unittest

import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent.parent.resolve()
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from interface_py import interface
from tests.functional.interface.test_helpers import SourceLoaderTestCase


class InterfaceHasNoConcreteLogicTestCase(SourceLoaderTestCase):
    
    def test_no_concrete_method(self):
        expected_message = "Method 'foo' in interface 'MyInterface' must have empty body."
        
        with self.assertRaises(TypeError) as context:
            
            @interface
            class MyInterface:
                
                def foo(self):
                    return "bar"
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_no_concrete_classmethod(self):
        expected_message = "Class method 'foo' in interface 'MyInterface' must have empty body."
        
        with self.assertRaises(TypeError) as context:
            
            @interface
            class MyInterface:
                
                @classmethod
                def foo(cls):
                    return "bar"
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_no_concrete_staticmethod(self):
        expected_message = "Static method 'foo' in interface 'MyInterface' must have empty body."
        
        with self.assertRaises(TypeError) as context:
            
            @interface
            class MyInterface:
                
                @staticmethod
                def foo():
                    return "bar"
            
        self.assertEqual(str(context.exception), expected_message)


if __name__ == "__main__":
    unittest.main()
