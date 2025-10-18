import unittest
from unittest import TestCase

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.parent.absolute())
sys.path.append(path)

from interface_py import interface


class MethodDuckTypingTestCase(TestCase):
    
    def setUp(self):
        
        @interface
        class _DuckInterface:
            def quack(self): ...
        
        self.DuckInterface = _DuckInterface
    
    
    def tearDown(self):
        del self.DuckInterface
    
    
    def test_valid_duck(self):

        class ValidDuck:
            
            def quack(self):
                return "QUACK"

        self.assertTrue(issubclass(ValidDuck, self.DuckInterface))
    
    
    def test_invalid_duck(self):
        
        class InvalidDuck:
            
            def read(self):
                return "Bar"

        self.assertFalse(issubclass(InvalidDuck, self.DuckInterface))


    def test_invalid_duck_method_signiture(self):
        
        class InvalidDuck:
            
            def quack(self, extra_param):
                return "Bar"

        self.assertFalse(issubclass(InvalidDuck, self.DuckInterface))
    
    
    def test_invalid_duck_staticmethod(self):

        class InvalidDuck:
            
            @staticmethod
            def quack(self):
                pass
        
        self.assertFalse(issubclass(InvalidDuck, self.DuckInterface))


    def test_invalid_duck_classmethod(self):

        class InvalidDuck:

            @classmethod
            def quack(self):
                pass 
        
        self.assertFalse(issubclass(InvalidDuck, self.DuckInterface))


    def test_invalid_duck_field(self):

        class InvalidDuck:
            quack = 2
        
        self.assertFalse(issubclass(InvalidDuck, self.DuckInterface))


    def test_invalid_duck_property(self):

        class InvalidDuck:

            @property
            def quack(self):
                return "Hi"
        
        self.assertFalse(issubclass(InvalidDuck, self.DuckInterface))


class StaticMethodDuckTypingTestCase(TestCase):
    
    def setUp(self):
        
        @interface
        class _DuckInterface:
            
            @staticmethod
            def quack(data, param): ...
        
        self.DuckInterface = _DuckInterface
    
    
    def tearDown(self):
        del self.DuckInterface
    
    
    def test_valid_duck(self):

        class ValidDuck:
            
            @staticmethod
            def quack(data, param):
                return data

        self.assertTrue(issubclass(ValidDuck, self.DuckInterface))


    def test_invalid_duck(self):
        
        class InvalidDuck:
            
            def read(self):
                return "Bar"

        self.assertFalse(issubclass(InvalidDuck, self.DuckInterface))
    

    def test_invalid_duck_method_signiture(self):
        
        class InvalidDuck:
            
            @staticmethod
            def quack(data, bad_param):
                return data

        self.assertFalse(issubclass(InvalidDuck, self.DuckInterface))
    
    
    def test_invalid_duck_method(self):

        class InvalidDuck:
            
            def quack(data, param):
                pass
        
        self.assertFalse(issubclass(InvalidDuck, self.DuckInterface))


    def test_invalid_duck_classmethod(self):

        class InvalidDuck:
            
            @classmethod
            def quack(data, param):
                pass
        
        self.assertFalse(issubclass(InvalidDuck, self.DuckInterface))


    def test_invalid_duck_field(self):

        class InvalidDuck:
            quack = 2
        
        self.assertFalse(issubclass(InvalidDuck, self.DuckInterface))


    def test_invalid_duck_property(self):

        class InvalidDuck:

            @property
            def quack(data, param):
                return "Hi"
        
        self.assertFalse(issubclass(InvalidDuck, self.DuckInterface))


class ClassMethodDuckTypingTestCase(TestCase):
    
    def setUp(self):
        
        @interface
        class _DuckInterface:
            
            @classmethod
            def quack(data, param): ...
        
        self.DuckInterface = _DuckInterface
    
    
    def tearDown(self):
        del self.DuckInterface
    

    def test_valid_duck(self):

        class ValidDuck:
            
            @classmethod
            def quack(data, param):
                return

        self.assertTrue(issubclass(ValidDuck, self.DuckInterface))


    def test_invalid_duck(self):
        
        class InvalidDuck:
            
            def read(self):
                return "Bar"

        self.assertFalse(issubclass(InvalidDuck, self.DuckInterface))
    

    def test_invalid_duck_method_signiture(self):
        
        class InvalidDuck:
            
            @classmethod
            def quack(data, wrong_param):
                return

        self.assertFalse(issubclass(InvalidDuck, self.DuckInterface))
    
    
    def test_invalid_duck_method(self):

        class InvalidDuck:
            
            def quack(data, param):
                pass
        
        self.assertFalse(issubclass(InvalidDuck, self.DuckInterface))


    def test_invalid_duck_staticmethod(self):

        class InvalidDuck:

            @staticmethod
            def quack(data, param):
                pass 
        
        self.assertFalse(issubclass(InvalidDuck, self.DuckInterface))


    def test_invalid_duck_field(self):

        class InvalidDuck:
            quack = 2
        
        self.assertFalse(issubclass(InvalidDuck, self.DuckInterface))


    def test_invalid_duck_property(self):

        class InvalidDuck:

            @property
            def quack(data, param):
                return "Hi"
        
        self.assertFalse(issubclass(InvalidDuck, self.DuckInterface))


class FieldThreeDotsDuckTypingTestCase(TestCase):

    def setUp(self):
        
        @interface
        class _DuckInterface:
            age = ...
        
        self.DuckInterface = _DuckInterface
    
    
    def tearDown(self):
        del self.DuckInterface
    

    def test_valid_duck(self):

        class ValidDuck:
            age = 8

        self.assertTrue(issubclass(ValidDuck, self.DuckInterface))


    def test_invalid_duck(self):
        
        class InvalidDuck:
            
            def read(self):
                return "Bar"

        self.assertFalse(issubclass(InvalidDuck, self.DuckInterface))
    
    
    def test_invalid_duck_method(self):

        class InvalidDuck:
            
            def age(self):
                pass
        
        self.assertFalse(issubclass(InvalidDuck, self.DuckInterface))
    
    
    def test_invalid_duck_staticmethod(self):

        class InvalidDuck:
            
            @staticmethod
            def age(self):
                return
        
        self.assertFalse(issubclass(InvalidDuck, self.DuckInterface))


    def test_invalid_duck_classmethod(self):

        class InvalidDuck:

            @classmethod
            def age(self):
                return "a" 
        
        self.assertFalse(issubclass(InvalidDuck, self.DuckInterface))


    def test_invalid_duck_property(self):

        class InvalidDuck:

            @property
            def age(self):
                return "Hi"
        
        self.assertFalse(issubclass(InvalidDuck, self.DuckInterface))


class PropertyDuckTypingTestCase(TestCase):

    def setUp(self):
        
        @interface
        class _DuckInterface:
            
            @property
            def age(self): ...
        
        self.DuckInterface = _DuckInterface
    
    
    def tearDown(self):
        del self.DuckInterface
    

    def test_valid_duck(self):

        class ValidDuck:
            
            @property
            def age(self):
                return 7

        self.assertTrue(issubclass(ValidDuck, self.DuckInterface))


    def test_invalid_duck(self):
        
        class InvalidDuck:
            
            def read(self):
                return "Bar"

        self.assertFalse(issubclass(InvalidDuck, self.DuckInterface))
    
    
    def test_invalid_duck_method(self):

        class InvalidDuck:

            def age(self):
                return "Hi"
        
        self.assertFalse(issubclass(InvalidDuck, self.DuckInterface))
    
    
    def test_invalid_duck_staticmethod(self):

        class InvalidDuck:
            
            @staticmethod
            def age(self):
                pass
        
        self.assertFalse(issubclass(InvalidDuck, self.DuckInterface))


    def test_invalid_duck_classmethod(self):

        class InvalidDuck:

            @classmethod
            def age(self):
                pass 
        
        self.assertFalse(issubclass(InvalidDuck, self.DuckInterface))


    def test_invalid_duck_field(self):

        class InvalidDuck:
            age = 2
        
        self.assertFalse(issubclass(InvalidDuck, self.DuckInterface))


class FieldEllipsisDuckTypingTestCase(FieldThreeDotsDuckTypingTestCase):

    def setUp(self):
        
        @interface
        class _DuckInterface:
            age = Ellipsis
        
        self.DuckInterface = _DuckInterface


class FieldAnnotationDuckTypingTestCase(FieldThreeDotsDuckTypingTestCase):

    def setUp(self):
        
        @interface
        class _DuckInterface:
            age: int
        
        self.DuckInterface = _DuckInterface


class FieldAnnotationThreeDotsDuckTypingTestCase(FieldThreeDotsDuckTypingTestCase):

    def setUp(self):
        
        @interface
        class _DuckInterface:
            age: int = ...
        
        self.DuckInterface = _DuckInterface


class FieldAnnotationEllipsisDuckTypingTestCase(FieldThreeDotsDuckTypingTestCase):

    def setUp(self):
        
        @interface
        class _DuckInterface:
            age: int = Ellipsis
        
        self.DuckInterface = _DuckInterface


class FieldTypeClassDuckTypingTestCase(FieldThreeDotsDuckTypingTestCase):

    def setUp(self):
        
        @interface
        class _DuckInterface:
            age = int
        
        self.DuckInterface = _DuckInterface


class FieldAnnotationTypeClassDuckTypingTestCase(FieldThreeDotsDuckTypingTestCase):

    def setUp(self):
        
        @interface
        class _DuckInterface:
            age: int = int
        
        self.DuckInterface = _DuckInterface


if __name__ == "__main__":
    unittest.main()
