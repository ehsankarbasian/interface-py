import unittest
from unittest import TestCase

import sys
from pathlib import Path
# find absolute project root
ROOT_PATH = Path(__file__).resolve().parents[2]
if str(ROOT_PATH) not in sys.path:
    sys.path.insert(0, str(ROOT_PATH))

from src import interface
from test.utils import load_interface_from_source


class InterfaceHasNoConcreteLogicTestCase(TestCase):
    
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
    
    
    def test_no_concrete_property(self):
        expected_message = "In interface 'MyInterface', property 'foo' must not define a getter."
        
        fake_source = '''
            from src import interface
            
            @interface
            class MyInterface:
                
                @property
                def foo(self):
                    return "bar"
        '''
            
        with self.assertRaises(TypeError) as context:
            load_interface_from_source(fake_source, "MyInterface")
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_no_concrete_property_getter(self):
        expected_message = "In interface 'MyInterface', property 'foo' must not define a getter."
        
        fake_source = '''
            from src import interface
            
            @interface
            class MyInterface:
                
                @property
                def foo(self):
                    pass
                
                @foo.getter
                def foo(self):
                    return "bar"
        '''
            
        with self.assertRaises(TypeError) as context:
            load_interface_from_source(fake_source, "MyInterface")

        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_no_concrete_property_setter(self):
        expected_message = "In interface 'MyInterface', property 'foo' must not define a setter."
        
        with self.assertRaises(TypeError) as context:
            
            @interface
            class MyInterface:
                
                @property
                def foo(self):
                    pass
                
                @foo.setter
                def foo(self, value):
                    print(f'set: {value}')
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_no_concrete_property_deleter(self):
        expected_message = "In interface 'MyInterface', property 'foo' must not define a deleter."

        with self.assertRaises(TypeError) as context:
            
            @interface
            class MyInterface:
                
                @property
                def foo(self):
                    pass
                
                @foo.deleter
                def foo(self, value):
                    print(f'delete: {value}')
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_no_concrete_property_getter_setter(self):
        expected_messages = '\n'.join([
            "In interface 'MyInterface', property 'foo' must not define a getter.",
            "In interface 'MyInterface', property 'foo' must not define a setter."
        ])
        
        fake_source = '''
            from src import interface
            
            @interface
            class MyInterface:
                
                @property
                def foo(self):
                    pass
                
                @foo.getter
                def foo(self):
                    print(f'get')
                
                @foo.setter
                def foo(self, value):
                    print(f'set: {value}')
        '''
            
        with self.assertRaises(TypeError) as context:
            load_interface_from_source(fake_source, "MyInterface")
        
        self.assertEqual(str(context.exception), expected_messages)
    
    
    def test_no_concrete_property_getter_deleter(self):
        expected_messages = '\n'.join([
            "In interface 'MyInterface', property 'foo' must not define a getter.",
            "In interface 'MyInterface', property 'foo' must not define a deleter."
        ])
        
        fake_source = '''
            from src import interface
            
            @interface
            class MyInterface:
                
                @property
                def foo(self):
                    pass
                
                @foo.getter
                def foo(self):
                    print(f'get')
                
                @foo.deleter
                def foo(self):
                    print(f'Delete')
        '''
        
        with self.assertRaises(TypeError) as context:
            load_interface_from_source(fake_source, "MyInterface")

        self.assertEqual(str(context.exception), expected_messages)
    
    
    def test_no_concrete_property_setter_deleter(self):
        expected_messages = '\n'.join([
            "In interface 'MyInterface', property 'foo' must not define a setter.",
            "In interface 'MyInterface', property 'foo' must not define a deleter."
        ])
        
        with self.assertRaises(TypeError) as context:
            
            @interface
            class MyInterface:
                
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
            "In interface 'MyInterface', property 'foo' must not define a getter.",
            "In interface 'MyInterface', property 'foo' must not define a setter.",
            "In interface 'MyInterface', property 'foo' must not define a deleter."
        ])
        
        fake_source = '''
            from src import interface
            
            @interface
            class MyInterface:
                
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
        '''
            
        with self.assertRaises(TypeError) as context:
            load_interface_from_source(fake_source, "MyInterface")
            
        self.assertEqual(str(context.exception), expected_messages)
    
    
    def test_no_concrete_property_propertybody_setter_deleter(self):
        expected_messages = '\n'.join([
            "In interface 'MyInterface', property 'foo' must not define a getter.",
            "In interface 'MyInterface', property 'foo' must not define a setter.",
            "In interface 'MyInterface', property 'foo' must not define a deleter."
        ])
        
        fake_source = '''
            from src import interface
            
            @interface
            class MyInterface:
                
                @property
                def foo(self):
                    print('Concrete')
                
                @foo.setter
                def foo(self, value):
                    print(f'set: {value}')
                
                @foo.deleter
                def foo(self):
                    print(f'Delete')
        '''
            
        with self.assertRaises(TypeError) as context:
            load_interface_from_source(fake_source, "MyInterface")
            
        self.assertEqual(str(context.exception), expected_messages)
    
    
    def test_no_concrete_property_propertybody_getter_setter_deleter(self):
        expected_messages = '\n'.join([
            "In interface 'MyInterface', property 'foo' must not define a getter.",
            "In interface 'MyInterface', property 'foo' must not define a setter.",
            "In interface 'MyInterface', property 'foo' must not define a deleter."
        ])
        

        fake_source = '''
            from src import interface
            
            @interface
            class MyInterface:
                
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
        '''
            
        with self.assertRaises(TypeError) as context:
            load_interface_from_source(fake_source, "MyInterface")
            
        self.assertEqual(str(context.exception), expected_messages)


if __name__ == "__main__":
    unittest.main()
