import unittest
from unittest import TestCase

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.absolute())
sys.path.append(path)

from src.interface_py import interface, concrete


class EmptyConcreteTestCase(TestCase):
    
    def setUp(self):
        
        @interface
        class EmptyInterface:
            pass
        
        self.EmptyInterface = EmptyInterface
        return super().setUp()
    
    
    def tearDown(self):
        del self.EmptyInterface
        return super().tearDown()
    
    
    def test_empty_interface_empty_concrete(self):
        
        @concrete
        class EmptyConcrete(self.EmptyInterface):
            pass
    
    
    def test_empty_interface_non_empty_concrete(self):
        
        @concrete
        class EmptyConcrete(self.EmptyInterface):
            x = 10
            
            def talk(self):
                print('hello')
                
            @property
            def state(self):
                return 'OK'


if __name__ == "__main__":
    unittest.main()
