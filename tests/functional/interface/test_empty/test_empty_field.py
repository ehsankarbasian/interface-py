import unittest
from unittest import TestCase

import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent.resolve()
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from interface_py import interface


class InterfaceCanDefineEmptyFieldTestCase(TestCase):
    
    def test_empty_ellipsis_field(self):
        
        @interface
        class MyInterface:
            x = ...
    
    
    def test_empty_typehint_field(self):
        
        @interface
        class MyInterface:
            x: int
    
    
    def test_empty_ellipsis_and_typehint_field(self):
        
        @interface
        class MyInterface:
            x: int = ...

    
    def test_empty_builtin_type_field(self):
        
        @interface
        class MyInterface:
            DataModel = dict
    
    
    def test_empty_custom_class_field(self):
        
        class MyCustomSerializer:
            pass
        
        @interface
        class MyInterface:
            DataModel = MyCustomSerializer


if __name__ == "__main__":
    unittest.main()
