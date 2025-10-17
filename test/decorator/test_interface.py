import unittest
from unittest import TestCase

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.absolute())
sys.path.append(path)

from interface_py import interface


class ـNonInterfaceParent:
    pass


class TestInterfaceDecorator(TestCase):

    def test_valid_single_interface_inheritance(self):
        
        @interface
        class ParentInterface:
            ...

        @interface
        class ChildInterface(ParentInterface):
            ...

        self.assertTrue(getattr(ChildInterface, "_is_interface_"))
    
    
    def test_valid_multiple_interface_inheritance(self):
        
        @interface
        class ParentInterface_1:
            ...
        
        @interface
        class ParentInterface_2:
            ...

        @interface
        class ChildInterface(ParentInterface_1, ParentInterface_2):
            ...

        self.assertTrue(getattr(ChildInterface, "_is_interface_"))
    
    
    def test_valid_chained_interface_inheritance(self):
        
        @interface
        class ParentInterface:
            ...
        
        @interface
        class MiddleInterface(ParentInterface):
            ...

        @interface
        class ChildInterface(MiddleInterface):
            ...

        self.assertTrue(getattr(MiddleInterface, "_is_interface_"))
        self.assertTrue(getattr(ChildInterface, "_is_interface_"))
    
    
    def test_valid_multiple_chained_interface_inheritance(self):
        
        @interface
        class ParentInterface_1:
            ...
        
        @interface
        class ParentInterface_2:
            ...
        
        @interface
        class ParentInterface_3:
            ...
        
        @interface
        class ParentInterface_4:
            ...
        
        @interface
        class MiddleInterface_1(ParentInterface_1, ParentInterface_2):
            ...
        
        @interface
        class MiddleInterface_2(ParentInterface_3, ParentInterface_4):
            ...

        @interface
        class ChildInterface(MiddleInterface_1, MiddleInterface_2):
            ...

        self.assertTrue(getattr(MiddleInterface_1, "_is_interface_"))
        self.assertTrue(getattr(MiddleInterface_2, "_is_interface_"))
        self.assertTrue(getattr(ChildInterface, "_is_interface_"))


    def test_invalid_interface_inheritance(self):
        expected_message = "In interface 'BadInterface', all parents must be interfaces. Found non-interface parent 'ـNonInterfaceParent'."
        
        with self.assertRaises(TypeError) as context:
            
            @interface
            class BadInterface(ـNonInterfaceParent):
                ...
        
        self.assertEqual(str(context.exception), expected_message)


if __name__ == "__main__":
    unittest.main()
