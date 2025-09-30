import unittest
from unittest import TestCase

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.absolute())
sys.path.append(path)

from interface import interface, InterfaceBase


class InterfaceCanDefineEmptyFieldTestCase(TestCase):
    
    def test_empty_ellipsis_field(self):
        
        @interface
        class MyInterface(InterfaceBase):
            x = ...
    
    
    def test_empty_typehint_field(self):
        
        @interface
        class MyInterface(InterfaceBase):
            x: int
    
    
    def test_empty_ellipsis_and_typehint_field(self):
        
        @interface
        class MyInterface(InterfaceBase):
            x: int = ...


if __name__ == "__main__":
    unittest.main()
