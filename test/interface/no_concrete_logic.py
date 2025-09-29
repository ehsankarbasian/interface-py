import unittest
from unittest import TestCase

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.absolute())
sys.path.append(path)

from interface import interface, InterfaceBase


class InterfaceHasNoConcreteLogicTestCase(TestCase):
    
    def test_no_concrete_method(self):
        expected_message = "Method 'foo' in interface 'MyInterface' must have empty body."
        
        with self.assertRaises(TypeError) as context:
            
            @interface
            class MyInterface(InterfaceBase):
                
                def foo(self):
                    return "bar"
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_no_concrete_classmethod(self):
        expected_message = "Class method 'foo' in interface 'MyInterface' must have empty body."
        
        with self.assertRaises(TypeError) as context:
            
            @interface
            class MyInterface(InterfaceBase):
                
                @classmethod
                def foo(cls):
                    return "bar"
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_no_concrete_staticmethod(self):
        expected_message = "Static method 'foo' in interface 'MyInterface' must have empty body."
        
        with self.assertRaises(TypeError) as context:
            
            @interface
            class MyInterface(InterfaceBase):
                
                @staticmethod
                def foo():
                    return "bar"
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_no_concrete_property(self):
        expected_message = "Property getter 'foo' in interface 'MyInterface' must have empty body."
        
        with self.assertRaises(TypeError) as context:
            
            @interface
            class MyInterface(InterfaceBase):
                
                @property
                def foo(self):
                    return "bar"
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_no_concrete_property_getter(self):
        expected_message = "Property getter 'foo' in interface 'MyInterface' must have empty body."
        
        with self.assertRaises(TypeError) as context:
            
            @interface
            class MyInterface(InterfaceBase):
                
                @property
                def foo(self):
                    pass
                
                @foo.getter
                def foo(self):
                    return "bar"
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_no_concrete_property_setter(self):
        expected_message = "Property setter 'foo' in interface 'MyInterface' must have empty body."
        
        with self.assertRaises(TypeError) as context:
            
            @interface
            class MyInterface(InterfaceBase):
                
                @property
                def foo(self):
                    pass
                
                @foo.setter
                def foo(self, value):
                    print(f'set: {value}')
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_no_concrete_property_deleter(self):
        expected_message = "Property deleter 'foo' in interface 'MyInterface' must have empty body."
        
        with self.assertRaises(TypeError) as context:
            
            @interface
            class MyInterface(InterfaceBase):
                
                @property
                def foo(self):
                    pass
                
                @foo.deleter
                def foo(self, value):
                    print(f'delete: {value}')
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_no_concrete_property_getter_setter(self):
        expected_messages = '\n'.join([
            "Property getter 'foo' in interface 'MyInterface' must have empty body.",
            "Property setter 'foo' in interface 'MyInterface' must have empty body."
        ])
        
        with self.assertRaises(TypeError) as context:
            
            @interface
            class MyInterface(InterfaceBase):
                
                @property
                def foo(self):
                    pass
                
                @foo.getter
                def foo(self):
                    print(f'get')
                
                @foo.setter
                def foo(self, value):
                    print(f'set: {value}')
            
        self.assertEqual(str(context.exception), expected_messages)
    
    
    def test_no_concrete_property_getter_deleter(self):
        expected_messages = '\n'.join([
            "Property getter 'foo' in interface 'MyInterface' must have empty body.",
            "Property deleter 'foo' in interface 'MyInterface' must have empty body."
        ])
        
        with self.assertRaises(TypeError) as context:
            
            @interface
            class MyInterface(InterfaceBase):
                
                @property
                def foo(self):
                    pass
                
                @foo.getter
                def foo(self):
                    print(f'get')
                
                @foo.deleter
                def foo(self):
                    print(f'Delete')
            
        self.assertEqual(str(context.exception), expected_messages)
    
    
    def test_no_concrete_property_setter_deleter(self):
        expected_messages = '\n'.join([
            "Property setter 'foo' in interface 'MyInterface' must have empty body.",
            "Property deleter 'foo' in interface 'MyInterface' must have empty body."
        ])
        
        with self.assertRaises(TypeError) as context:
            
            @interface
            class MyInterface(InterfaceBase):
                
                @property
                def foo(self):
                    pass
                
                @foo.setter
                def foo(self, value):
                    print(f'set: {value}')
                
                @foo.deleter
                def foo(self):
                    print(f'Delete')
            
        self.assertEqual(str(context.exception), expected_messages)
    
    
    def test_no_concrete_property_getter_setter_deleter(self):
        expected_messages = '\n'.join([
            "Property getter 'foo' in interface 'MyInterface' must have empty body.",
            "Property setter 'foo' in interface 'MyInterface' must have empty body.",
            "Property deleter 'foo' in interface 'MyInterface' must have empty body."
        ])
        
        with self.assertRaises(TypeError) as context:
            
            @interface
            class MyInterface(InterfaceBase):
                
                @property
                def foo(self):
                    pass
                
                @foo.getter
                def foo(self):
                    print(f'get')
                
                @foo.setter
                def foo(self, value):
                    print(f'set: {value}')
                
                @foo.deleter
                def foo(self):
                    print(f'Delete')
            
        self.assertEqual(str(context.exception), expected_messages)
    
    
    def test_no_concrete_property_propertybody_setter_deleter(self):
        expected_messages = '\n'.join([
            "Property getter 'foo' in interface 'MyInterface' must have empty body.",
            "Property setter 'foo' in interface 'MyInterface' must have empty body.",
            "Property deleter 'foo' in interface 'MyInterface' must have empty body."
        ])
        
        with self.assertRaises(TypeError) as context:
            
            @interface
            class MyInterface(InterfaceBase):
                
                @property
                def foo(self):
                    print('Concrete')
                
                @foo.setter
                def foo(self, value):
                    print(f'set: {value}')
                
                @foo.deleter
                def foo(self):
                    print(f'Delete')
            
        self.assertEqual(str(context.exception), expected_messages)
    
    
    def test_no_concrete_property_propertybody_getter_setter_deleter(self):
        expected_messages = '\n'.join([
            "Property getter 'foo' in interface 'MyInterface' must have empty body.",
            "Property setter 'foo' in interface 'MyInterface' must have empty body.",
            "Property deleter 'foo' in interface 'MyInterface' must have empty body."
        ])
        
        with self.assertRaises(TypeError) as context:
            
            @interface
            class MyInterface(InterfaceBase):
                
                @property
                def foo(self):
                    print('Concrete')
                
                @foo.getter
                def foo(self):
                    print(f'get')
                
                @foo.setter
                def foo(self, value):
                    print(f'set: {value}')
                
                @foo.deleter
                def foo(self):
                    print(f'Delete')
            
        self.assertEqual(str(context.exception), expected_messages)


if __name__ == "__main__":
    unittest.main()
