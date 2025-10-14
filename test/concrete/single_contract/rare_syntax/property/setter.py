import unittest
from unittest import TestCase

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.parent.parent.parent.absolute())
sys.path.append(path)

from src import interface, concrete


class PropertySetterContractTestCase(TestCase):
    
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
        
        def val_setter(self, value):
            self.t = value
        
        func = property(val, val_setter)
        
        @concrete
        class MyConcrete(self.MyInterface):
            val = func
        
        MyConcrete()
    
    
    def test_instantiate_good_concrete_2(self):
        
        def val(self):
            return "The Value"
        
        def val_setter(self, value):
            self.t = value
        
        func = property(val, val_setter)
        
        MyConcrete = concrete(
            type("MyConcrete", (self.MyInterface, ), {"val": func})
        )
        
        MyConcrete()
    
    
    def test_instantiate_good_concrete_3(self):
        
        def val(self):
            return "The Value"
        
        def val_setter(self, value):
            self.t = value
        
        func = property(val, val_setter)
        
        def add_method(cls):
            cls.val = func
            return cls
        
        @concrete
        @add_method
        class MyConcrete(self.MyInterface):
            pass
        
        MyConcrete()
    
    
    def test_instance_works_1(self):
        
        def val(self):
            return "The Value"
        
        def val_setter(self, value):
            self.t = value
        
        func = property(val, val_setter)
        
        @concrete
        class MyConcrete(self.MyInterface):
            val = func
        
        instance = MyConcrete()
        instance.val = 'NEW'
        self.assertEqual(instance.t, 'NEW')
    
    
    def test_instance_works_2(self):
        
        def val(self):
            return "The Value"
        
        def val_setter(self, value):
            self.t = value
        
        func = property(val, val_setter)
        
        MyConcrete = concrete(
            type("MyConcrete", (self.MyInterface, ), {"val": func})
        )
        
        instance = MyConcrete()
        instance.val = 'NEW'
        self.assertEqual(instance.t, 'NEW')
    
    
    def test_instance_works_3(self):
        
        def val(self):
            return "The Value"
        
        def val_setter(self, value):
            self.t = value
        
        func = property(val, val_setter)
        
        def add_method(cls):
            cls.val = func
            return cls
        
        @concrete
        @add_method
        class MyConcrete(self.MyInterface):
            pass
        
        instance = MyConcrete()
        instance.val = 'NEW'
        self.assertEqual(instance.t, 'NEW')


class PropertyContractTypeTestCase(PropertySetterContractTestCase):

    def setUp(self):
        
        @property
        def val(self):
            pass
        
        _MyInterface = interface(
            type("_MyInterface", (), {"val": val})
        )
        
        self.MyInterface = _MyInterface


class PropertyContractDecoratorTestCase(PropertySetterContractTestCase):

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


class PropertyContractMetaTestCase(PropertySetterContractTestCase):

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
