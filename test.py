import unittest
from unittest import TestCase

from interface import interface, concrete, InterfaceBase


# @interface
# class HumanInterface(InterfaceBase):
#     def talk(self): pass
#     def walk(self): ...

# @interface
# class MilitaryHuman(HumanInterface):
#     def shoot(self): ...

# @concrete
# class Commander(MilitaryHuman):
#     def talk(self): print("talking")
#     def walk(self): print("walking")
#     def shoot(self): print("shooting")

# Raises error:
# InterfaceBase()
# Human()
# MilitaryHuman()

# c = Commander()
# c.talk()


class InterfaceInstantiationTestCase(TestCase):
    
    def setUp(self):
        
        @interface
        class Level_1_Interface_dot(InterfaceBase): ...
        @interface
        class Level_2_Interface_dot(Level_1_Interface_dot): ...
        @interface
        class Level_3_Interface_dot(Level_2_Interface_dot): ...
        
        self.Level_1_Interface_dot = Level_1_Interface_dot
        self.Level_2_Interface_dot = Level_2_Interface_dot
        self.Level_3_Interface_dot = Level_3_Interface_dot
        
        @interface
        class Level_1_Interface_pass(InterfaceBase): pass
        @interface
        class Level_2_Interface_pass(Level_1_Interface_pass): pass
        @interface
        class Level_3_Interface_pass(Level_2_Interface_pass): pass
        
        self.Level_1_Interface_pass = Level_1_Interface_pass
        self.Level_2_Interface_pass = Level_2_Interface_pass
        self.Level_3_Interface_pass = Level_3_Interface_pass
    
    
    def tearDown(self):
        
        del self.Level_1_Interface_dot
        del self.Level_2_Interface_dot
        del self.Level_3_Interface_dot
        
        del self.Level_1_Interface_pass
        del self.Level_2_Interface_pass
        del self.Level_3_Interface_pass
        
        return super().tearDown()
    
    
    def test_no_instance_from_InterfaceBase(self):
        self.assertRaises(Exception, InterfaceBase)
    
    def test_no_instance_from_interface_level_1(self):
        self.assertRaises(Exception, self.Level_1_Interface_dot)
        self.assertRaises(Exception, self.Level_1_Interface_pass)
    
    def test_no_instance_from_interface_level_2(self):
        self.assertRaises(Exception, self.Level_2_Interface_dot)
        self.assertRaises(Exception, self.Level_2_Interface_pass)
    
    def test_no_instance_from_interface_level_3(self):
        self.assertRaises(Exception, self.Level_3_Interface_dot)
        self.assertRaises(Exception, self.Level_3_Interface_pass)
    
    def test_raised_exception_is_TypeError(self):
        self.assertRaises(TypeError, InterfaceBase)
        
        self.assertRaises(TypeError, self.Level_1_Interface_dot)
        self.assertRaises(TypeError, self.Level_1_Interface_pass)
        
        self.assertRaises(TypeError, self.Level_2_Interface_dot)
        self.assertRaises(TypeError, self.Level_2_Interface_pass)
        
        self.assertRaises(TypeError, self.Level_3_Interface_dot)
        self.assertRaises(TypeError, self.Level_3_Interface_pass)
    
    def test_check_exception_message_InterfaceBase(self):
        expected_message = "Cannot instantiate interface class 'InterfaceBase'"
        with self.assertRaises(Exception) as context:
            InterfaceBase()
        self.assertEqual(str(context.exception), expected_message)
    
    def test_check_exception_message_level_1(self):
        expected_message = "Cannot instantiate interface class 'Level_1_Interface_dot'"
        with self.assertRaises(Exception) as context:
            self.Level_1_Interface_dot()
        self.assertEqual(str(context.exception), expected_message)
        
        expected_message = "Cannot instantiate interface class 'Level_1_Interface_pass'"
        with self.assertRaises(Exception) as context:
            self.Level_1_Interface_pass()
        self.assertEqual(str(context.exception), expected_message)
    
    def test_check_exception_message_level_2(self):
        expected_message = "Cannot instantiate interface class 'Level_2_Interface_dot'"
        with self.assertRaises(Exception) as context:
            self.Level_2_Interface_dot()
        self.assertEqual(str(context.exception), expected_message)
        
        expected_message = "Cannot instantiate interface class 'Level_2_Interface_pass'"
        with self.assertRaises(Exception) as context:
            self.Level_2_Interface_pass()
        self.assertEqual(str(context.exception), expected_message)
    
    def test_check_exception_message_level_3(self):
        expected_message = "Cannot instantiate interface class 'Level_3_Interface_dot'"
        with self.assertRaises(Exception) as context:
            self.Level_3_Interface_dot()
        self.assertEqual(str(context.exception), expected_message)
        
        expected_message = "Cannot instantiate interface class 'Level_3_Interface_pass'"
        with self.assertRaises(Exception) as context:
            self.Level_3_Interface_pass()
        self.assertEqual(str(context.exception), expected_message)


class InterfaceHasNoConcreteLogicTestCase(TestCase):
    
    def test_no_concrete_method(self):
        expected_message = "Method 'foo' in interface 'MyInterface' must have empty body."
        
        with self.assertRaises(TypeError) as context:
            
            @interface
            class MyInterface(InterfaceBase):
                
                def foo(self):
                    return "bar"
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_no_concrete_classmethod(self):
        expected_message = "Class method 'foo' in interface 'MyInterface' must have empty body."
        
        with self.assertRaises(TypeError) as context:
            
            @interface
            class MyInterface(InterfaceBase):
                
                @classmethod
                def foo(cls):
                    return "bar"
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_no_concrete_staticmethod(self):
        expected_message = "Static method 'foo' in interface 'MyInterface' must have empty body."
        
        with self.assertRaises(TypeError) as context:
            
            @interface
            class MyInterface(InterfaceBase):
                
                @staticmethod
                def foo():
                    return "bar"
            
        self.assertEqual(str(context.exception), expected_message)
    
    
    def test_no_concrete_property(self):
        expected_message = "Property 'foo' in interface 'MyInterface' must have empty body."
        
        with self.assertRaises(TypeError) as context:
            
            @interface
            class MyInterface(InterfaceBase):
                
                @property
                def foo(self):
                    return "bar"
            
        self.assertEqual(str(context.exception), expected_message)


if __name__ == "__main__":
    unittest.main()
