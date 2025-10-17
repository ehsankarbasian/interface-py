import unittest
from unittest import TestCase

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.parent.parent.parent.absolute())
sys.path.append(path)

from interface_py import interface, concrete


class PropertyDeleterContractTestCase(TestCase):
    
    def setUp(self):
        
        def val(self):
            ...
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
        
        def val_deleter(self):
            del self.t
        
        func = property(val, fdel=val_deleter)
        
        @concrete
        class MyConcrete(self.MyInterface):
            val = func
        
        MyConcrete()
    
    
    def test_instantiate_good_concrete_2(self):
        
        def val(self):
            return "The Value"
        
        def val_deleter(self):
            del self.t
        
        func = property(val, fdel=val_deleter)
        
        MyConcrete = concrete(
            type("MyConcrete", (self.MyInterface, ), {"val": func})
        )
        
        MyConcrete()
    
    
    def test_instantiate_good_concrete_3(self):
        
        def val(self):
            return "The Value"
        
        def val_deleter(self):
            del self.t
        
        func = property(val, fdel=val_deleter)
        
        def add_method(cls):
            cls.val = func
            return cls
        
        @concrete
        @add_method
        class MyConcrete(self.MyInterface):
            pass
        
        MyConcrete()
    
    
    def test_deleter_works_1(self):
        
        def val(self):
            return "The Value"
        
        def val_deleter(self):
            del self.t
        
        func = property(val, fdel=val_deleter)
        
        @concrete
        class MyConcrete(self.MyInterface):
            val = func
        
        instance = MyConcrete()
        instance.t = 'NEW'
        self.assertEqual(instance.t, 'NEW')
        
        del instance.val
        is_t_deleted = not hasattr(instance, 't')
        self.assertTrue(is_t_deleted)
    
    
    def test_deleter_works_2(self):
        
        def val(self):
            return "The Value"
        
        def val_deleter(self):
            del self.t
        
        func = property(val, fdel=val_deleter)
        
        MyConcrete = concrete(
            type("MyConcrete", (self.MyInterface, ), {"val": func})
        )
        
        instance = MyConcrete()
        instance.t = 'NEW'
        self.assertEqual(instance.t, 'NEW')
        
        del instance.val
        is_t_deleted = not hasattr(instance, 't')
        self.assertTrue(is_t_deleted)
    
    
    def test_deleter_works_3(self):
        
        def val(self):
            return "The Value"
        
        def val_deleter(self):
            del self.t
        
        func = property(val, fdel=val_deleter)
        
        def add_method(cls):
            cls.val = func
            return cls
        
        @concrete
        @add_method
        class MyConcrete(self.MyInterface):
            pass
        
        instance = MyConcrete()
        instance.t = 'NEW'
        self.assertEqual(instance.t, 'NEW')
        
        del instance.val
        is_t_deleted = not hasattr(instance, 't')
        self.assertTrue(is_t_deleted)


class PropertyContractTypeTestCase(PropertyDeleterContractTestCase):

    def setUp(self):
        
        @property
        def val(self):
            pass
        
        _MyInterface = interface(
            type("_MyInterface", (), {"val": val})
        )
        
        self.MyInterface = _MyInterface


class PropertyContractDecoratorTestCase(PropertyDeleterContractTestCase):

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


class PropertyContractMetaTestCase(PropertyDeleterContractTestCase):

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
