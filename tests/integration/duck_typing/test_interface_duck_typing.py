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


if __name__ == "__main__":
    unittest.main()
