import unittest
from unittest import TestCase

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.parent.parent.absolute())
sys.path.append(path)

from src import interface, concrete


class FieldContractElipsisTestCase(TestCase):
    
    def setUp(self):
        
        @interface
        class _MyInterface:
            x = ...
        
        self.MyInterface = _MyInterface
    
    
    def tearDown(self):
        del self.MyInterface
        return super().tearDown()
    
    
    def test_success_1(self):
        @concrete
        class MyConcrete(self.MyInterface):
            x: int = 5
    
    
    def test_success_2(self):
        @concrete
        class MyConcrete(self.MyInterface):
            x: str = 5
    
    
    def test_success_3(self):
        @concrete
        class MyConcrete(self.MyInterface):
            x: str = None
    
    
    def test_success_4(self):
        @concrete
        class MyConcrete(self.MyInterface):
            def foo(self): ...
            x: int = 2
    
    
    def test_success_5(self):
        @concrete
        class MyConcrete(self.MyInterface):
            def foo(self): ...
            x: str = 2
    
    
    def test_success_6(self):
        @concrete
        class MyConcrete(self.MyInterface):
            def foo(self): ...
            x: int = None
    
    
    def test_success_7(self):
        MyConcrete = concrete(
            type("MyConcrete", (self.MyInterface, ), {"x": 0})
        )
    
    
    def test_success_8(self):
        MyConcrete = concrete(
            type("MyConcrete", (self.MyInterface, ), {"x": None})
        )
    
    
    def test_success_9(self):
        
        def add_x(cls):
            cls.x = 2
            return cls

        @concrete
        @add_x
        class MyConcrete(self.MyInterface):
            pass
    
    
    def test_instantiate_good_concrete_1(self):
        @concrete
        class MyConcrete(self.MyInterface):
            x: int = 5
        
        MyConcrete()
    

    def test_instantiate_good_concrete_2(self):
        @concrete
        class MyConcrete(self.MyInterface):
            x: str = 5
        
        MyConcrete()
    

    def test_instantiate_good_concrete_3(self):
        @concrete
        class MyConcrete(self.MyInterface):
            x: str = None
        
        MyConcrete()
    

    def test_instantiate_good_concrete_4(self):
        @concrete
        class MyConcrete(self.MyInterface):
            def foo(self): ...
            x: int = 2
        
        MyConcrete()
    

    def test_instantiate_good_concrete_5(self):
        @concrete
        class MyConcrete(self.MyInterface):
            def foo(self): ...
            x: str = 2
        
        MyConcrete()
    

    def test_instantiate_good_concrete_6(self):
        @concrete
        class MyConcrete(self.MyInterface):
            def foo(self): ...
            x: int = None
        
        MyConcrete()
    
    
    def test_instantiate_good_concrete_7(self):
        MyConcrete = concrete(
            type("MyConcrete", (self.MyInterface, ), {"x": 0})
        )
        MyConcrete()
    
    
    def test_instantiate_good_concrete_8(self):
        MyConcrete = concrete(
            type("MyConcrete", (self.MyInterface, ), {"x": None})
        )
        MyConcrete()
        
        
    def test_instantiate_good_concrete_9(self):

        def add_x(cls):
            cls.x = 2
            return cls

        @concrete
        @add_x
        class MyConcrete(self.MyInterface):
            pass
        
        MyConcrete()
    
    
    def test_no_implement_contract_1(self):
        expected_message = "Concrete class 'MyConcrete' must implement contracts: x"
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                pass
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_no_implement_contract_2(self):
        expected_message = "Concrete class 'MyConcrete' must implement contracts: x"
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                x = Ellipsis
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_no_implement_contract_3(self):
        expected_message = "Concrete class 'MyConcrete' must implement contracts: x"
        
        with self.assertRaises(TypeError) as context:
            @concrete
            class MyConcrete(self.MyInterface):
                x = ...
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_no_implement_contract_4(self):
        expected_message = "Concrete class 'MyConcrete' must implement contracts: x"
        
        with self.assertRaises(TypeError) as context:
            MyConcrete = concrete(
                type("MyConcrete", (self.MyInterface, ), {})
            )
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_no_implement_contract_5(self):
        expected_message = "Concrete class 'MyConcrete' must implement contracts: x"
        
        with self.assertRaises(TypeError) as context:
            MyConcrete = concrete(
                type("MyConcrete", (self.MyInterface, ), {"x": ...})
            )
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_no_implement_contract_6(self):
        expected_message = "Concrete class 'MyConcrete' must implement contracts: x"
        
        with self.assertRaises(TypeError) as context:
            MyConcrete = concrete(
                type("MyConcrete", (self.MyInterface, ), {"x": Ellipsis})
            )
            
        self.assertEqual(str(context.exception), expected_message)


class FieldContractTypeThreeDotsTestCase(FieldContractElipsisTestCase):

    def setUp(self):
        
        _MyInterface = interface(
            type("_MyInterface", (), {"x": ...})
        )
        
        self.MyInterface = _MyInterface


class FieldContractTypeEllipsisTestCase(FieldContractElipsisTestCase):

    def setUp(self):
        
        _MyInterface = interface(
            type("_MyInterface", (), {"x": Ellipsis})
        )
        
        self.MyInterface = _MyInterface


class FieldContractClassDecoratorTestCase(FieldContractElipsisTestCase):
    
    def setUp(self):
        
        def add_x(cls):
            cls.x = ...
            return cls
        
        @interface
        @add_x
        class _MyInterface:
            pass
        
        self.MyInterface = _MyInterface


class FieldContractMetaClassTestCase(FieldContractElipsisTestCase):
    
    def setUp(self):
        
        class Meta(type):
            def __new__(mcls, name, bases, attrs):
                attrs["x"] = ...
                return super().__new__(mcls, name, bases, attrs)
        
        @interface
        class _MyInterface(metaclass=Meta):
            pass
        
        self.MyInterface = _MyInterface


if __name__ == "__main__":
    unittest.main()
