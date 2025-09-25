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
        class Level_1_Interface(InterfaceBase): ...
        @interface
        class Level_2_Interface(Level_1_Interface): ...
        @interface
        class Level_3_Interface(Level_2_Interface): ...
        
        self.Level_1_Interface = Level_1_Interface
        self.Level_2_Interface = Level_2_Interface
        self.Level_3_Interface = Level_3_Interface
    
    
    def tearDown(self):
        del self.Level_1_Interface
        del self.Level_2_Interface
        del self.Level_3_Interface
    
    
    def test_no_instance_from_InterfaceBase(self):
        self.assertRaises(Exception, InterfaceBase)
    
    def test_no_instance_from_interface_level_1(self):
        self.assertRaises(Exception, self.Level_1_Interface)
    
    def test_no_instance_from_interface_level_2(self):
        self.assertRaises(Exception, self.Level_2_Interface)
    
    def test_no_instance_from_interface_level_3(self):
        self.assertRaises(Exception, self.Level_3_Interface)


if __name__ == "__main__":
    unittest.main()
