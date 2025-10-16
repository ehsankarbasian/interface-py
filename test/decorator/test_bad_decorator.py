import unittest
from unittest import TestCase

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.absolute())
sys.path.append(path)

from src import interface, concrete


class ـNonInterfaceParent:
    pass


def bad_validator_decorator(cls):
    cls._is_interface_ = None
    cls.__validate__()
    return cls


class TestConcreteDecorator(TestCase):

    def test_interface_bad_validator_decorator(self):
        expected_message = "Class must be decorated with @interface or @concrete"
        
        with self.assertRaises(TypeError) as context:
            
            @bad_validator_decorator
            @interface
            class MyInterface:
                ...
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_concrete_bad_validator_decorator(self):
        expected_message = "Class must be decorated with @interface or @concrete"
        
        with self.assertRaises(TypeError) as context:
            
            @interface
            class MyInterface:
                ...
            
            @bad_validator_decorator
            class BadConcrete(MyInterface):
                ...
        
        self.assertEqual(str(context.exception), expected_message)


if __name__ == "__main__":
    unittest.main()
