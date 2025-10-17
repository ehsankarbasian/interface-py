import unittest
from unittest import TestCase

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.absolute())
sys.path.append(path)

from interface_py import interface, concrete


class ـNonInterfaceParent:
    pass


class TestConcreteDecorator(TestCase):

    def test_valid_concrete_with_one_only_interface_parent(self):
        
        @interface
        class MyInterface:
            ...

        @concrete
        class MyConcrete(MyInterface):
            ...

        self.assertFalse(getattr(MyConcrete, "_is_interface_"))
    
    
    def test_valid_concrete_with_one_interface_parents(self):
        
        @interface
        class MyInterface:
            ...

        @concrete
        class MyConcrete(MyInterface, ـNonInterfaceParent):
            ...

        self.assertFalse(getattr(MyConcrete, "_is_interface_"))
    
    
    def test_valid_concrete_with_multiple_only_interface_parents(self):
        
        @interface
        class MyInterface_1:
            ...
        
        @interface
        class MyInterface_2:
            ...

        @concrete
        class MyConcrete(MyInterface_1, MyInterface_2):
            ...

        self.assertFalse(getattr(MyConcrete, "_is_interface_"))
    
    
    def test_valid_concrete_with_multiple_interface_parents(self):
        
        @interface
        class MyInterface_1:
            ...
        
        @interface
        class MyInterface_2:
            ...

        @concrete
        class MyConcrete_1(MyInterface_1, ـNonInterfaceParent, MyInterface_2):
            ...
        
        @concrete
        class MyConcrete_2(ـNonInterfaceParent, MyInterface_1, MyInterface_2):
            ...

        self.assertFalse(getattr(MyConcrete_1, "_is_interface_"))
        self.assertFalse(getattr(MyConcrete_2, "_is_interface_"))


    def test_invalid_concrete_without_interface_parent(self):
        expected_message = "Concrete class 'BadConcrete' must inherit from at least one interface."
        
        with self.assertRaises(TypeError) as context:
            
            @concrete
            class BadConcrete(ـNonInterfaceParent):
                ...
        
        self.assertEqual(str(context.exception), expected_message)


if __name__ == "__main__":
    unittest.main()
