import unittest
from unittest import TestCase

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.parent.parent.absolute())
sys.path.append(path)

from interface_py import interface, concrete



class MethodContractPositionalArgsTestCase(TestCase):
    
    def test_success_star(self):
        
        @interface
        class MyInterface:
            
            @staticmethod
            def foo(par_1, *, par_2):
                pass
        
        @concrete
        class MyConcrete(MyInterface):
            
            @staticmethod
            def foo(par_1, *, par_2):
                return "Bar"
        
        MyConcrete()
    
    
    def test_success_slash(self):
        
        @interface
        class MyInterface:
            
            @staticmethod
            def foo(par_1, /, par_2):
                pass
        
        @concrete
        class MyConcrete(MyInterface):
            
            @staticmethod
            def foo(par_1, /, par_2):
                return "Bar"
        
        MyConcrete()
        
    
    def test_success_star_and_slash(self):
        
        @interface
        class MyInterface:
            
            @staticmethod
            def foo(par_1, par_2, /, par_3, par_4, par_5, *, par_6, par_7):
                pass
        
        @concrete
        class MyConcrete(MyInterface):
            
            @staticmethod
            def foo(par_1, par_2, /, par_3, par_4, par_5, *, par_6, par_7):
                return "Bar"
        
        MyConcrete()
        
    
    def test_error_star_not_mentioned(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected (par_1, *, par_2), got (par_1, par_2)."
        
        @interface
        class MyInterface:
            
            @staticmethod
            def foo(par_1, *, par_2):
                pass
        
        with self.assertRaises(TypeError) as context:
            
            @concrete
            class MyConcrete(MyInterface):
                
                @staticmethod
                def foo(par_1, par_2):
                    return "Bar"
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_error_star_wrong_position(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected (par_1, *, par_2, par_3), got (par_1, par_2, *, par3)."
        
        @interface
        class MyInterface:
            
            @staticmethod
            def foo(par_1, *, par_2, par_3):
                pass
        
        with self.assertRaises(TypeError) as context:
            
            @concrete
            class MyConcrete(MyInterface):
                
                @staticmethod
                def foo(par_1, par_2, *, par3):
                    return "Bar"
        
        self.assertEqual(str(context.exception), expected_message)
            

    def test_error_slash_not_mentioned(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected (par_1, /, par_2), got (par_1, par_2)."
        
        @interface
        class MyInterface:
            
            @staticmethod
            def foo(par_1, /, par_2):
                pass
        
        with self.assertRaises(TypeError) as context:
            
            @concrete
            class MyConcrete(MyInterface):
                
                @staticmethod
                def foo(par_1, par_2):
                    return "Bar"
        
        self.assertEqual(str(context.exception), expected_message)
        
        
    def test_error_slash_wrong_position(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected (par_1, /, par_2, par_3), got (par_1, par_2, /, par_3)."
        
        @interface
        class MyInterface:
            
            @staticmethod
            def foo(par_1, /, par_2, par_3):
                pass
        
        with self.assertRaises(TypeError) as context:
            
            @concrete
            class MyConcrete(MyInterface):
                
                @staticmethod
                def foo(par_1, par_2, /, par_3):
                    return "Bar"
        
        self.assertEqual(str(context.exception), expected_message)


    def test_error_slash_and_star_not_mentioned_slash(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected (par_1, par_2, /, par_3, par_4, par_5, *, par_6, par_7), got (par_1, par_2, par_3, par_4, par_5, *, par_6, par_7)."

        @interface
        class MyInterface:
            
            @staticmethod
            def foo(par_1, par_2, /, par_3, par_4, par_5, *, par_6, par_7):
                pass
        
        with self.assertRaises(TypeError) as context:
            
            @concrete
            class MyConcrete(MyInterface):
                
                @staticmethod
                def foo(par_1, par_2, par_3, par_4, par_5, *, par_6, par_7):
                    return "Bar"
        
        self.assertEqual(str(context.exception), expected_message)
        
        
    def test_error_slash_and_star_not_mentioned_star(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected (par_1, par_2, /, par_3, par_4, par_5, *, par_6, par_7), got (par_1, par_2, /, par_3, par_4, par_5, par_6, par_7)."

        @interface
        class MyInterface:
            
            @staticmethod
            def foo(par_1, par_2, /, par_3, par_4, par_5, *, par_6, par_7):
                pass
        
        with self.assertRaises(TypeError) as context:
            
            @concrete
            class MyConcrete(MyInterface):
                
                @staticmethod
                def foo(par_1, par_2, /, par_3, par_4, par_5, par_6, par_7):
                    return "Bar"
        
        self.assertEqual(str(context.exception), expected_message)
        
        
    def test_error_slash_and_star_not_mentioned_both(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected (par_1, par_2, /, par_3, par_4, par_5, *, par_6, par_7), got (par_1, par_2, par_3, par_4, par_5, par_6, par_7)."

        @interface
        class MyInterface:
            
            @staticmethod
            def foo(par_1, par_2, /, par_3, par_4, par_5, *, par_6, par_7):
                pass
        
        with self.assertRaises(TypeError) as context:
            
            @concrete
            class MyConcrete(MyInterface):
                
                @staticmethod
                def foo(par_1, par_2, par_3, par_4, par_5, par_6, par_7):
                    return "Bar"
        
        self.assertEqual(str(context.exception), expected_message)
        
    
    def test_error_slash_and_star_wrong_position_slash(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected (par_1, par_2, /, par_3, par_4, par_5, *, par_6, par_7), got (par_1, par_2, par_3, /, par_4, par_5, *, par_6, par_7)."
        
        @interface
        class MyInterface:
            
            @staticmethod
            def foo(par_1, par_2, /, par_3, par_4, par_5, *, par_6, par_7):
                pass
        
        with self.assertRaises(TypeError) as context:
            
            @concrete
            class MyConcrete(MyInterface):
                
                @staticmethod
                def foo(par_1, par_2, par_3, /, par_4, par_5, *, par_6, par_7):
                    return "Bar"
        
        self.assertEqual(str(context.exception), expected_message)
        

    def test_error_slash_and_star_wrong_position_star(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected (par_1, par_2, /, par_3, par_4, par_5, *, par_6, par_7), got (par_1, par_2, /, par_3, *, par_4, par_5, par_6, par_7)."
        
        @interface
        class MyInterface:
            
            @staticmethod
            def foo(par_1, par_2, /, par_3, par_4, par_5, *, par_6, par_7):
                pass
        
        with self.assertRaises(TypeError) as context:
            
            @concrete
            class MyConcrete(MyInterface):
                
                @staticmethod
                def foo(par_1, par_2, /, par_3, *, par_4, par_5, par_6, par_7):
                    return "Bar"
        
        self.assertEqual(str(context.exception), expected_message)
        

    def test_error_slash_and_star_wrong_position_both(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected (par_1, par_2, /, par_3, par_4, par_5, *, par_6, par_7), got (par_1, /, par_2, par_3, par_4, *, par_5, par_6, par_7)."
        
        @interface
        class MyInterface:
            
            @staticmethod
            def foo(par_1, par_2, /, par_3, par_4, par_5, *, par_6, par_7):
                pass
        
        with self.assertRaises(TypeError) as context:
            
            @concrete
            class MyConcrete(MyInterface):
                
                @staticmethod
                def foo(par_1, /, par_2, par_3, par_4, *, par_5, par_6, par_7):
                    return "Bar"
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_error_has_extra_slash_1(self):

        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected (par_1, par_2, *, par_3), got (par_1, /, par_2, *, par_3)."
        
        @interface
        class MyInterface:
            
            @staticmethod
            def foo(par_1, par_2, *, par_3):
                pass
        
        with self.assertRaises(TypeError) as context:
            
            @concrete
            class MyConcrete(MyInterface):
                
                @staticmethod
                def foo(par_1, /, par_2, *, par_3):
                    return "Bar"
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_error_has_extra_slash_2(self):

        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected (par_1, par_2, par_3), got (par_1, par_2, /, par_3)."
        
        @interface
        class MyInterface:
            
            @staticmethod
            def foo(par_1, par_2, par_3):
                pass
        
        with self.assertRaises(TypeError) as context:
            
            @concrete
            class MyConcrete(MyInterface):
                
                @staticmethod
                def foo(par_1, par_2, /, par_3):
                    return "Bar"
        
        self.assertEqual(str(context.exception), expected_message)


    def test_error_has_extra_star_1(self):

        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected (par_1, /, par_2, par_3), got (par_1, /, par_2, *, par_3)."
        
        @interface
        class MyInterface:
            
            @staticmethod
            def foo(par_1, /, par_2, par_3):
                pass
        
        with self.assertRaises(TypeError) as context:
            
            @concrete
            class MyConcrete(MyInterface):
                
                @staticmethod
                def foo(par_1, /, par_2, *, par_3):
                    return "Bar"
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_error_has_extra_star_2(self):

        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected (par_1, par_2, par_3), got (par_1, par_2, *, par_3)."
        
        @interface
        class MyInterface:
            
            @staticmethod
            def foo(par_1, par_2, par_3):
                pass
        
        with self.assertRaises(TypeError) as context:
            
            @concrete
            class MyConcrete(MyInterface):
                
                @staticmethod
                def foo(par_1, par_2, *, par_3):
                    return "Bar"
        
        self.assertEqual(str(context.exception), expected_message)


    def test_error_has_extra_both(self):

        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected (par_1, par_2, par_3), got (par_1, /, par_2, *, par_3)."
        
        @interface
        class MyInterface:
            
            @staticmethod
            def foo(par_1, par_2, par_3):
                pass
        
        with self.assertRaises(TypeError) as context:
            
            @concrete
            class MyConcrete(MyInterface):
                
                @staticmethod
                def foo(par_1, /, par_2, *, par_3):
                    return "Bar"
        
        self.assertEqual(str(context.exception), expected_message)


class StaticMethodContractPassTestCase(TestCase):
    
    def setUp(self):
        
        def foo(par_1, par_2):
            pass
        func = staticmethod(foo)
        
        @interface
        class _MyInterface:
            foo = func
        
        self.MyInterface = _MyInterface
    
    
    def tearDown(self):
        del self.MyInterface
        return super().tearDown()
    
    
    def test_success_1(self):

        def foo(par_1, par_2):
            return f'{par_1} {par_2}'
        func = staticmethod(foo)

        @concrete
        class MyConcrete(self.MyInterface):
            foo = func
    
    
    def test_success_2(self):

        @staticmethod
        def foo(par_1, par_2):
            return f'{par_1} {par_2}'

        MyConcrete = concrete(
            type("MyConcrete", (self.MyInterface, ), {"foo": foo})
        )
    
    
    def test_success_3(self):

        @staticmethod
        def foo(par_1, par_2):
            return f'{par_1} {par_2}'

        def add_method(cls):
            cls.foo = foo
            return cls

        @concrete
        @add_method
        class MyConcrete(self.MyInterface):
            pass
    
    
    def test_instantiate_good_concrete_1(self):

        def foo(par_1, par_2):
            return f'{par_1} {par_2}'
        func = staticmethod(foo)

        @concrete
        class MyConcrete(self.MyInterface):
            foo = func
        
        MyConcrete()

    
    def test_instantiate_good_concrete_2(self):

        @staticmethod
        def foo(par_1, par_2):
            return f'{par_1} {par_2}'

        MyConcrete = concrete(
            type("MyConcrete", (self.MyInterface, ), {"foo": foo})
        )
        
        MyConcrete()
    
    
    def test_instantiate_good_concrete_3(self):

        @staticmethod
        def foo(par_1, par_2):
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
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected (par_1, par_2), got (par_1)."
        
        with self.assertRaises(TypeError) as context:

            def foo(par_1):
                return par_1
            func = staticmethod(foo)

            @concrete
            class MyConcrete(self.MyInterface):
                foo = func
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_bad_params_2(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected (par_1, par_2), got (par_1)."
        
        with self.assertRaises(TypeError) as context:

            @staticmethod
            def foo(par_1):
                return par_1

            MyConcrete = concrete(
                type("MyConcrete", (self.MyInterface, ), {"foo": foo})
            )
        
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_bad_params_3(self):
        expected_message = "Signature mismatch for 'foo' in concrete 'MyConcrete': expected (par_1, par_2), got (par_1)."
        
        with self.assertRaises(TypeError) as context:

            @staticmethod
            def foo(par_1):
                return par_1

            def add_method(cls):
                cls.foo = foo
                return cls

            @concrete
            @add_method
            class MyConcrete(self.MyInterface):
                pass
        
        self.assertEqual(str(context.exception), expected_message)


class StaticMethodContractTypeTestCase(StaticMethodContractPassTestCase):
    
    def setUp(self):
        
        @staticmethod
        def foo(par_1, par_2):
            ...

        _MyInterface = interface(
            type("_MyInterface", (), {"foo": foo})
        )
        
        self.MyInterface = _MyInterface


class StaticMethodContractClassDecoratorTestCase(StaticMethodContractPassTestCase):
    
    def setUp(self):
        
        @staticmethod
        def foo(par_1, par_2):
            ...

        def add_method(cls):
            cls.foo = foo
            return cls

        @interface
        @add_method
        class _MyInterface:
            pass
        
        self.MyInterface = _MyInterface


class StaticMethodContractMetaTestCase(StaticMethodContractPassTestCase):
    
    def setUp(self):
        
        @staticmethod
        def foo(par_1, par_2):
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
