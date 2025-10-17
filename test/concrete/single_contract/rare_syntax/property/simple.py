import unittest
from unittest import TestCase

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.parent.parent.parent.absolute())
sys.path.append(path)

from src.interface_py import interface, concrete


class PropertyContractTestCase(TestCase):
    
    def setUp(self):
        
        def val(self):
            pass
        func = property(val)
        
        @interface
        class _MyInterface:
            val = func
        
        self.MyInterface = _MyInterface
    
    
    def tearDown(self):
        del self.MyInterface
        return super().tearDown()
    
    
    def test_instantiate_good_concrete_1(self):
        
        def val(self):
            return "The Value"
        func = property(val)
        
        @concrete
        class MyConcrete(self.MyInterface):
            val = func
        
        MyConcrete()
    
    
    def test_instantiate_good_concrete_2(self):
        
        @property
        def val(self):
            return "The Value"
        
        MyConcrete = concrete(
            type("MyConcrete", (self.MyInterface, ), {"val": val})
        )
        
        MyConcrete()
    
    
    def test_instantiate_good_concrete_3(self):
        
        @property
        def val(self):
            return "The Value"
        
        def add_method(cls):
            cls.val = val
            return cls
        
        @concrete
        @add_method
        class MyConcrete(self.MyInterface):
            pass
        
        MyConcrete()


class PropertyContractTypeTestCase(PropertyContractTestCase):

    def setUp(self):
        
        @property
        def val(self):
            pass
        
        _MyInterface = interface(
            type("_MyInterface", (), {"val": val})
        )
        
        self.MyInterface = _MyInterface


class PropertyContractDecoratorTestCase(PropertyContractTestCase):

    def setUp(self):
        
        @property
        def val(self):
            pass
        
        def add_method(cls):
            cls.val = val
            return cls
        
        @interface
        @add_method
        class _MyInterface:
            pass
        
        self.MyInterface = _MyInterface


class PropertyContractMetaTestCase(PropertyContractTestCase):

    def setUp(self):
        
        @property
        def val(self):
            ...
        
        class Meta(type):
            def __new__(mcls, name, bases, attrs):
                attrs['val'] = val
                return super().__new__(mcls, name, bases, attrs)
        
        @interface
        class _MyInterface(metaclass=Meta):
            pass
        
        self.MyInterface = _MyInterface


if __name__ == "__main__":
    unittest.main()
