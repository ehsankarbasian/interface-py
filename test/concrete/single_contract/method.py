import unittest
from unittest import TestCase

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.parent.absolute())
sys.path.append(path)

from src import interface, concrete


class MethodContractPassTestCase(TestCase):
    
    def setUp(self):
        
        @interface
        class _MyInterface:
            def foo(self, par_1, par_2):
                pass
        
        self.MyInterface = _MyInterface
    
    
    def tearDown(self):
        del self.MyInterface
        return super().tearDown()
    
    
    def test_success(self):
        @concrete
        class MyConcrete(self.MyInterface):
            def foo(self, par_1, par_2):
                return f'{par_1} {par_2}'
    
    
    def test_instantiate_good_concrete(self):
        @concrete
        class MyConcrete(self.MyInterface):
            def foo(self, par_1, par_2):
                return f'{par_1} {par_2}'
        
        MyConcrete()
    
    
    def test_not_the_same_params(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected (self, par_1, par_2), got (self, par_1)."
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                def foo(self, par_1):
                    return par_1
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_no_implement_contract(self):
        expected_message = "Concrete class 'MyConcrete' must implement contracts: foo"
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                pass
            
        self.assertEqual(str(context.exception), expected_message)


class ConstructorContractPassTestCase(TestCase):
    
    def setUp(self):
        
        @interface
        class _MyInterface:
            def __init__(self, a, b):
                pass
        
        self.MyInterface = _MyInterface
    
    
    def tearDown(self):
        del self.MyInterface
        return super().tearDown()


    def test_success(self):
        @concrete
        class MyConcrete(self.MyInterface):
            def __init__(self, a, b):
                self.a = a
                self.b = b

    
    def test_instantiate_good_concrete(self):
        @concrete
        class MyConcrete(self.MyInterface):
            def __init__(self, a, b):
                self.a = a
                self.b = b
        
        MyConcrete(1, 2)
    
    
    def test_not_the_same_params(self):
        expected_message = "Signature mismatch for '__init__' in concrete 'MyConcrete': expected (self, a, b), got (self, a)."
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                def __init__(self, a):
                    self.a = a
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_no_implement_contract(self):
        expected_message = "Concrete class 'MyConcrete' must implement contracts: __init__"
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                pass
            
        self.assertEqual(str(context.exception), expected_message)


class MagicMethodContractPassTestCase(TestCase):
    
    def setUp(self):
        
        @interface
        class _MyInterface:
            def __add__(self, var):
                pass
        
        self.MyInterface = _MyInterface
    
    
    def tearDown(self):
        del self.MyInterface
        return super().tearDown()


    def test_success(self):
        @concrete
        class MyConcrete(self.MyInterface):
            def __add__(self, var):
                return f'{var} foo'

    
    def test_instantiate_good_concrete(self):
        @concrete
        class MyConcrete(self.MyInterface):
            def __add__(self, var):
                return f'{var} foo'
        
        MyConcrete()
    
    
    def test_no_implement_contract(self):
        expected_message = "Concrete class 'MyConcrete' must implement contracts: __add__"
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                pass
            
        self.assertEqual(str(context.exception), expected_message)


class MethodContractEllipsisTestCase(MethodContractPassTestCase):

    def setUp(self):
        
        @interface
        class _MyInterface:
            def foo(self, par_1, par_2):
                ...
        
        self.MyInterface = _MyInterface


class ConstructorContractEllipsisTestCase(ConstructorContractPassTestCase):

    def setUp(self):
        
        @interface
        class _MyInterface:
            def __init__(self, a, b):
                ...
        
        self.MyInterface = _MyInterface


class MagicMethodContractEllipsisTestCase(MagicMethodContractPassTestCase):

    def setUp(self):
        
        @interface
        class _MyInterface:
            def __add__(self, var):
                ...
        
        self.MyInterface = _MyInterface


class MethodContractDocStringTestCase(MethodContractPassTestCase):

    def setUp(self):
        
        @interface
        class _MyInterface:
            def foo(self, par_1, par_2):
                """ The Docstring """
    
        self.MyInterface = _MyInterface


class ConstructorContractDocStringTestCase(ConstructorContractPassTestCase):

    def setUp(self):
        
        @interface
        class _MyInterface:
            def __init__(self, a, b):
                """ The DocString """
    
        self.MyInterface = _MyInterface


class MagicMethodContractPassTestCase(MagicMethodContractPassTestCase):

    def setUp(self):
        
        @interface
        class _MyInterface:
            def __add__(self, var):
                """ The DocString """
    
        self.MyInterface = _MyInterface



if __name__ == "__main__":
    unittest.main()
