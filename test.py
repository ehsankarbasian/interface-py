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


if __name__ == "__main__":
    unittest.main()
