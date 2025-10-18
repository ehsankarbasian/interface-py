import unittest
from unittest import TestCase

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.parent.parent.absolute())
sys.path.append(path)

from interface_py import interface, concrete


class MethodContractPassTestCase(TestCase):
    
    def setUp(self):
        
        def foo(self, par_1, par_2):
            pass
        func = foo
        
        @interface
        class _MyInterface:
            foo = func
        
        self.MyInterface = _MyInterface
    
    
    def tearDown(self):
        del self.MyInterface
        return super().tearDown()
    
    
    def test_success_1(self):
        
        def foo(self, par_1, par_2):
            return f'{par_1} {par_2}'
        func = foo
        
        @concrete
        class MyConcrete(self.MyInterface):
            foo = func
    
    
    def test_success_2(self):
        
        def foo(self, par_1, par_2):
            return f'{par_1} {par_2}'
        
        MyConcrete = concrete(
            type("MyConcrete", (self.MyInterface, ), {"foo": foo})
        )
    
    
    def test_success_3(self):
        
        def foo(self, par_1, par_2):
            return f'{par_1} {par_2}'
        
        def add_method(cls):
            cls.foo = foo
            return cls
        
        @concrete
        @add_method
        class MyConcrete(self.MyInterface):
            pass
    
    
    def test_instantiate_good_concrete_1(self):
        
        def foo(self, par_1, par_2):
            return f'{par_1} {par_2}'
        func = foo
        
        @concrete
        class MyConcrete(self.MyInterface):
            foo = func
        
        MyConcrete()
    
    
    def test_instantiate_good_concrete_2(self):
        
        def foo(self, par_1, par_2):
            return f'{par_1} {par_2}'
        
        MyConcrete = concrete(
            type("MyConcrete", (self.MyInterface, ), {"foo": foo})
        )
        
        MyConcrete()
    
    
    def test_instantiate_good_concrete_3(self):
        
        def foo(self, par_1, par_2):
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
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected (self, par_1, par_2), got (self, par_1)."
        
        def foo(self, par_1):
            return f'{par_1}'
        func = foo
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                foo = func
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_bad_params_2(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected (self, par_1, par_2), got (self)."
        
        def foo(self):
            pass
        func = foo
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                foo = func
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_bad_params_3(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected (self, par_1, par_2), got (self, par_2)."
        
        def foo(self, par_2):
            ...
        func = foo
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                foo = func
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_bad_params_4(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected (self, par_1, par_2), got (self, par_2, bad_par)."
        
        def foo(self, par_2, bad_par):
            return par_2
        func = foo
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                foo = func
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_bad_params_5(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected (self, par_1, par_2), got (self, par_1)."
        
        def foo(self, par_1):
            return f'{par_1}'
        
        with self.assertRaises(TypeError) as context:
            MyConcrete = concrete(
                type("MyConcrete", (self.MyInterface, ), {"foo": foo})
            )
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_bad_params_6(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected (self, par_1, par_2), got (self)."
        
        def foo(self):
            pass
        
        with self.assertRaises(TypeError) as context:
            MyConcrete = concrete(
                type("MyConcrete", (self.MyInterface, ), {"foo": foo})
            )
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_bad_params_7(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected (self, par_1, par_2), got (self, par_2)."
        
        def foo(self, par_2):
            ...
        
        with self.assertRaises(TypeError) as context:
            MyConcrete = concrete(
                type("MyConcrete", (self.MyInterface, ), {"foo": foo})
            )
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_bad_params_8(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected (self, par_1, par_2), got (self, par_2, bad_par)."
        
        def foo(self, par_2, bad_par):
            return par_2
        
        with self.assertRaises(TypeError) as context:
            MyConcrete = concrete(
                type("MyConcrete", (self.MyInterface, ), {"foo": foo})
            )
        
        self.assertEqual(str(context.exception), expected_message)

    
    def test_bad_params_9(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected (self, par_1, par_2), got (self, par_1)."
        
        with self.assertRaises(TypeError) as context:

            def foo(self, par_1):
                return f'{par_1}'
            
            def add_method(cls):
                cls.foo = foo
                return cls

            @concrete
            @add_method
            class MyConcrete(self.MyInterface):
                pass
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_bad_params_10(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected (self, par_1, par_2), got (self)."
        
        with self.assertRaises(TypeError) as context:

            def foo(self):
                pass
            
            def add_method(cls):
                cls.foo = foo
                return cls

            @concrete
            @add_method
            class MyConcrete(self.MyInterface):
                pass
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_bad_params_11(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected (self, par_1, par_2), got (self, par_2)."
        
        with self.assertRaises(TypeError) as context:

            def foo(self, par_2):
                ...
            
            def add_method(cls):
                cls.foo = foo
                return cls

            @concrete
            @add_method
            class MyConcrete(self.MyInterface):
                pass
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_bad_params_12(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected (self, par_1, par_2), got (self, par_2, bad_par)."
        
        with self.assertRaises(TypeError) as context:

            def foo(self, par_2, bad_par):
                return par_2
            
            def add_method(cls):
                cls.foo = foo
                return cls

            @concrete
            @add_method
            class MyConcrete(self.MyInterface):
                pass
        
        self.assertEqual(str(context.exception), expected_message)
    

class ConstructorContractPassTestCase(TestCase):
    
    def setUp(self):
        
        def __init__(self, a, b):
            pass
        func = __init__
        
        @interface
        class _MyInterface:
            __init__ = func
            
        self.MyInterface = _MyInterface
    
    
    def tearDown(self):
        del self.MyInterface
        return super().tearDown()
    
    
    def test_success_1(self):
        
        def __init__(self, a, b):
            self.a = a
            self.b = b
        func = __init__
        
        @concrete
        class MyConcrete(self.MyInterface):
            __init__ = func
    
    
    def test_success_2(self):
        
        def __init__(self, a, b):
            self.a = a
            self.b = b
        
        MyConcrete = concrete(
            type("MyConcrete", (self.MyInterface, ), {"__init__": __init__})
        )
    
    
    def test_success_3(self):
        
        def __init__(self, a, b):
            self.a = a
            self.b = b
        
        def add_method(cls):
            cls.__init__ = __init__
            return cls
        
        @concrete
        @add_method
        class MyConcrete(self.MyInterface):
            pass

    
    def test_instantiate_good_concrete_1(self):
        
        def __init__(self, a, b):
            self.a = a
            self.b = b
        func = __init__
        
        @concrete
        class MyConcrete(self.MyInterface):
            __init__ = func
        
        MyConcrete(1, 2)
    
    
    def test_instantiate_good_concrete_2(self):
        
        def __init__(self, a, b):
            self.a = a
            self.b = b
        
        MyConcrete = concrete(
            type("MyConcrete", (self.MyInterface, ), {"__init__": __init__})
        )
        
        MyConcrete(1, 2)
    
    
    def test_instantiate_good_concrete_3(self):
        
        def __init__(self, a, b):
            self.a = a
            self.b = b
        
        def add_method(cls):
            cls.__init__ = __init__
            return cls
        
        @concrete
        @add_method
        class MyConcrete(self.MyInterface):
            pass
        
        MyConcrete(1, 2)
    
    
    def test_bad_params_1(self):
        expected_message = "Signature mismatch for '__init__' in concrete 'MyConcrete': expected (self, a, b), got (sf, a)."
        
        def __init__(sf, a):
            self.a = a
        func = __init__
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                __init__ = func
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_bad_params_2(self):
        expected_message = "Signature mismatch for '__init__' in concrete 'MyConcrete': expected (self, a, b), got (self, A, b)."
        
        def __init__(self, A, b):
            pass
        func = __init__
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                __init__ = func
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_bad_params_3(self):
        expected_message = "Signature mismatch for '__init__' in concrete 'MyConcrete': expected (self, a, b), got (slf, a, b, c)."
        
        def __init__(slf, a, b, c):
            self.a = a
        func = __init__
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                __init__ = func
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_bad_params_4(self):
        expected_message = "Signature mismatch for '__init__' in concrete 'MyConcrete': expected (self, a, b), got (sf, a)."
        
        def __init__(sf, a):
            self.a = a
        
        with self.assertRaises(TypeError) as context:
            MyConcrete = concrete(
                type("MyConcrete", (self.MyInterface, ), {"__init__": __init__})
            )
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_bad_params_5(self):
        expected_message = "Signature mismatch for '__init__' in concrete 'MyConcrete': expected (self, a, b), got (self, A, b)."
        
        def __init__(self, A, b):
            pass
        
        with self.assertRaises(TypeError) as context:
            MyConcrete = concrete(
                type("MyConcrete", (self.MyInterface, ), {"__init__": __init__})
            )
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_bad_params_6(self):
        expected_message = "Signature mismatch for '__init__' in concrete 'MyConcrete': expected (self, a, b), got (slf, a, b, c)."
        
        def __init__(slf, a, b, c):
            self.a = a
        
        with self.assertRaises(TypeError) as context:
            MyConcrete = concrete(
                type("MyConcrete", (self.MyInterface, ), {"__init__": __init__})
            )
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_bad_params_7(self):
        expected_message = "Signature mismatch for '__init__' in concrete 'MyConcrete': expected (self, a, b), got (sf, a)."
        
        with self.assertRaises(TypeError) as context:
            
            def __init__(sf, a):
                self.a = a
            
            def add_method(cls):
                cls.__init__ = __init__
                return cls

            @concrete
            @add_method
            class MyConcrete(self.MyInterface):
                pass
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_bad_params_8(self):
        expected_message = "Signature mismatch for '__init__' in concrete 'MyConcrete': expected (self, a, b), got (self, A, b)."
        
        with self.assertRaises(TypeError) as context:
            
            def __init__(self, A, b):
                pass
            
            def add_method(cls):
                cls.__init__ = __init__
                return cls

            @concrete
            @add_method
            class MyConcrete(self.MyInterface):
                pass
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_bad_params_9(self):
        expected_message = "Signature mismatch for '__init__' in concrete 'MyConcrete': expected (self, a, b), got (slf, a, b, c)."
        
        with self.assertRaises(TypeError) as context:
            
            def __init__(slf, a, b, c):
                self.a = a
            
            def add_method(cls):
                cls.__init__ = __init__
                return cls

            @concrete
            @add_method
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


    def test_success_1(self):
        @concrete
        class MyConcrete(self.MyInterface):
            def __add__(self, var):
                return f'{var} foo'
    
    
    def test_success_2(self):
        
        def __add__(self, var):
            return f'{var} foo'
        
        MyConcrete = concrete(
            type("MyConcrete", (self.MyInterface, ), {"__add__": __add__})
        )


    def test_success_3(self):
        
        def __add__(self, var):
            return f'{var} foo'
        
        def add_method(cls):
            cls.__add__ = __add__
            return cls
        
        @concrete
        @add_method
        class MyConcrete(self.MyInterface):
            pass

    
    def test_instantiate_good_concrete_1(self):
        @concrete
        class MyConcrete(self.MyInterface):
            def __add__(self, var):
                return f'{var} foo'
        
        MyConcrete()
    
    
    def test_instantiate_good_concrete_2(self):
        
        def __add__(self, var):
            return f'{var} foo'
        
        MyConcrete = concrete(
            type("MyConcrete", (self.MyInterface, ), {"__add__": __add__})
        )
        
        MyConcrete()
    
    
    def test_instantiate_good_concrete_3(self):
        
        def __add__(self, var):
            return f'{var} foo'
        
        def add_method(cls):
            cls.__add__ = __add__
            return cls
        
        @concrete
        @add_method
        class MyConcrete(self.MyInterface):
            pass
        
        MyConcrete()
    
    
    def test_bad_params_1(self):
        expected_message = "Signature mismatch for '__add__' in concrete 'MyConcrete': expected (self, var), got (self, a, b)."
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                def __add__(self, a, b):
                    return a + b
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_bad_params_2(self):
        expected_message = "Signature mismatch for '__add__' in concrete 'MyConcrete': expected (self, var), got (self, a)."
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                def __add__(self, a):
                    return a
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_bad_params_3(self):
        expected_message = "Signature mismatch for '__add__' in concrete 'MyConcrete': expected (self, var), got (self)."
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                def __add__(self):
                    return
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_bad_params_4(self):
        expected_message = "Signature mismatch for '__add__' in concrete 'MyConcrete': expected (self, var), got (self, a, b)."
        
        with self.assertRaises(TypeError) as context:
            def __add__(self, a, b):
                return f'{a+b} foo'
            
            MyConcrete = concrete(
                type("MyConcrete", (self.MyInterface, ), {"__add__": __add__})
            )
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_bad_params_5(self):
        expected_message = "Signature mismatch for '__add__' in concrete 'MyConcrete': expected (self, var), got (self, a)."
        
        with self.assertRaises(TypeError) as context:
            def __add__(self, a):
                return f'{a} foo'
            
            MyConcrete = concrete(
                type("MyConcrete", (self.MyInterface, ), {"__add__": __add__})
            )
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_bad_params_6(self):
        expected_message = "Signature mismatch for '__add__' in concrete 'MyConcrete': expected (self, var), got (self)."
        
        with self.assertRaises(TypeError) as context:
            def __add__(self):
                return f'foo'
            
            MyConcrete = concrete(
                type("MyConcrete", (self.MyInterface, ), {"__add__": __add__})
            )
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_bad_params_7(self):
        expected_message = "Signature mismatch for '__add__' in concrete 'MyConcrete': expected (self, var), got (self, a, b)."
        
        with self.assertRaises(TypeError) as context:
            
            def __add__(self, a, b):
                return a + b
            
            def add_method(cls):
                cls.__add__ = __add__
                return cls
            
            @concrete
            @add_method
            class MyConcrete(self.MyInterface):
                pass
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_bad_params_8(self):
        expected_message = "Signature mismatch for '__add__' in concrete 'MyConcrete': expected (self, var), got (self, a)."
        
        with self.assertRaises(TypeError) as context:
            
            def __add__(self, a):
                return a
            
            def add_method(cls):
                cls.__add__ = __add__
                return cls
            
            @concrete
            @add_method
            class MyConcrete(self.MyInterface):
                pass
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_bad_params_9(self):
        expected_message = "Signature mismatch for '__add__' in concrete 'MyConcrete': expected (self, var), got (self)."
        
        with self.assertRaises(TypeError) as context:
            
            def __add__(self):
                return
            
            def add_method(cls):
                cls.__add__ = __add__
                return cls
            
            @concrete
            @add_method
            class MyConcrete(self.MyInterface):
                pass
        
        self.assertEqual(str(context.exception), expected_message)
    
    
class MethodContractTypeTestCase(MethodContractPassTestCase):
    
    def setUp(self):
        
        def foo(self, par_1, par_2):
            pass
        
        _MyInterface = interface(
            type("_MyInterface", (), {"foo": foo})
        )
        
        self.MyInterface = _MyInterface


class ConstructorContractTypeTestCase(ConstructorContractPassTestCase):
    
    def setUp(self):
        
        def __init__(self, a, b):
            pass
        
        _MyInterface = interface(
            type("_MyInterface", (), {"__init__": __init__})
        )
        
        self.MyInterface = _MyInterface


class MagicMethodContractTypeTestCase(MagicMethodContractPassTestCase):
    
    def setUp(self):
        
        def __add__(self, var):
            pass
        
        _MyInterface = interface(
            type("_MyInterface", (), {"__add__": __add__})
        )
        
        self.MyInterface = _MyInterface


class MethodContractClassDecoratorTestCase(MethodContractPassTestCase):

    def setUp(self):
        
        def foo(self, par_1, par_2):
            pass
        
        def add_method(cls):
            cls.foo = foo
            return cls
        
        @interface
        @add_method
        class _MyInterface:
            pass
        
        self.MyInterface = _MyInterface


class ConstructorContractClassDecoratorTestCase(ConstructorContractPassTestCase):

    def setUp(self):
        
        def __init__(self, a, b):
            pass
        
        def add_method(cls):
            cls.__init__ = __init__
            return cls
        
        @interface
        @add_method
        class _MyInterface:
            pass
        
        self.MyInterface = _MyInterface


class MagicMethodContractClassDecoratorTestCase(MagicMethodContractPassTestCase):

    def setUp(self):
        
        def __add__(self, var):
            pass
        
        def add_method(cls):
            cls.__add__ = __add__
            return cls
        
        @interface
        @add_method
        class _MyInterface:
            pass
        
        self.MyInterface = _MyInterface


class MethodContractMetaTestCase(MethodContractPassTestCase):

    def setUp(self):
        
        def foo(self, par_1, par_2):
            pass
        
        class Meta(type):
            def __new__(mcls, name, bases, attrs):
                attrs['foo'] = foo
                return super().__new__(mcls, name, bases, attrs)

        @interface
        class _MyInterface(metaclass=Meta):
            pass
        
        self.MyInterface = _MyInterface


class ConstructorContractMetaTestCase(ConstructorContractPassTestCase):

    def setUp(self):
        
        def __init__(self, a, b):
            pass
        
        class Meta(type):
            def __new__(mcls, name, bases, attrs):
                attrs['__init__'] = __init__
                return super().__new__(mcls, name, bases, attrs)

        @interface
        class _MyInterface(metaclass=Meta):
            pass
        
        self.MyInterface = _MyInterface


class MagicMethodContractMetaTestCase(MagicMethodContractPassTestCase):

    def setUp(self):
        
        def __add__(self, var):
            pass
        
        class Meta(type):
            def __new__(mcls, name, bases, attrs):
                attrs['__add__'] = __add__
                return super().__new__(mcls, name, bases, attrs)

        @interface
        class _MyInterface(metaclass=Meta):
            pass
        
        self.MyInterface = _MyInterface


if __name__ == "__main__":
    unittest.main()
