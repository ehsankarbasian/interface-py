import unittest
from unittest import TestCase

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.parent.parent.absolute())
sys.path.append(path)

from src import interface, concrete


class ClassMethodContractPassTestCase(TestCase):
    
    def setUp(self):
        
        def foo(cls, par_1, par_2):
            pass
        func = classmethod(foo)
        
        @interface
        class _MyInterface:
            foo = func
        
        self.MyInterface = _MyInterface
    
    
    def tearDown(self):
        del self.MyInterface
        return super().tearDown()
    
    
    def test_success_1(self):

        def foo(cls, par_1, par_2):
            return f'{par_1} {par_2}'
        func = classmethod(foo)
        
        @concrete
        class MyConcrete(self.MyInterface):
            foo = func
    
    
    def test_success_2(self):

        @classmethod
        def foo(cls, par_1, par_2):
            return f'{par_1} {par_2}'
        
        MyConcrete = concrete(
            type("MyConcrete", (self.MyInterface, ), {"foo": foo})
        )
        
    
    def test_success_3(self):

        @classmethod
        def foo(cls, par_1, par_2):
            return f'{par_1} {par_2}'
        
        def add_method(cls):
            cls.foo = foo
            return cls

        @concrete
        @add_method
        class MyConcrete(self.MyInterface):
            pass
    
    
    def test_instantiate_good_concrete_1(self):

        def foo(cls, par_1, par_2):
            return f'{par_1} {par_2}'
        func = classmethod(foo)
        
        @concrete
        class MyConcrete(self.MyInterface):
            foo = func
        
        MyConcrete()
    
    
    def test_instantiate_good_concrete_2(self):

        @classmethod
        def foo(cls, par_1, par_2):
            return f'{par_1} {par_2}'
        
        MyConcrete = concrete(
            type("MyConcrete", (self.MyInterface, ), {"foo": foo})
        )
        
        MyConcrete()
    
    
    def test_instantiate_good_concrete_3(self):

        @classmethod
        def foo(cls, par_1, par_2):
            return f'{par_1} {par_2}'
        
        def add_method(cls):
            cls.foo = foo
            return cls

        @concrete
        @add_method
        class MyConcrete(self.MyInterface):
            pass
        
        MyConcrete()
    
    
    def test_bad_params_1(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected (cls, par_1, par_2), got (cls, par_1)."
        
        with self.assertRaises(TypeError) as context:

            def foo(cls, par_1):
                return par_1
            func = classmethod(foo)
            
            @concrete
            class MyConcrete(self.MyInterface):
                foo = func
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_bad_params_2(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected (cls, par_1, par_2), got (cls, par_1)."
        
        with self.assertRaises(TypeError) as context:

            @classmethod
            def foo(cls, par_1):
                return par_1
            
            MyConcrete = concrete(
                type("MyConcrete", (self.MyInterface, ), {"foo": foo})
            )
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_bad_params_3(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected (cls, par_1, par_2), got (cls, par_1)."
        
        with self.assertRaises(TypeError) as context:

            @classmethod
            def foo(cls, par_1):
                return par_1
            
            def add_method(cls):
                cls.foo = foo
                return cls

            @concrete
            @add_method
            class MyConcrete(self.MyInterface):
                pass
        
        self.assertEqual(str(context.exception), expected_message)


class ClassMethodContractTypeTestCase(ClassMethodContractPassTestCase):

    def setUp(self):
        
        @classmethod
        def foo(cls, par_1, par_2):
            ...

        _MyInterface = interface(
            type("_MyInterface", (), {"foo": foo})
        )
        
        self.MyInterface = _MyInterface


class ClassMethodContractClassDecoratorTestCase(ClassMethodContractPassTestCase):

    def setUp(self):
        
        @classmethod
        def foo(cls, par_1, par_2):
            ...

        def add_method(cls):
            cls.foo = foo
            return cls

        @interface
        @add_method
        class _MyInterface:
            pass
        
        self.MyInterface = _MyInterface


class ClassMethodContractMetaTestCase(ClassMethodContractPassTestCase):

    def setUp(self):
        
        @classmethod
        def foo(cls, par_1, par_2):
            ...
        
        class Meta(type):
            def __new__(mcls, name, bases, attrs):
                attrs['foo'] = foo
                return super().__new__(mcls, name, bases, attrs)

        @interface
        class _MyInterface(metaclass=Meta):
            pass
        
        self.MyInterface = _MyInterface


if __name__ == "__main__":
    unittest.main()
