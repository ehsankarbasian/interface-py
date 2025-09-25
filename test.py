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
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    
    def test_no_instance_from_InterfaceBase(self):
        self.assertRaises(Exception, InterfaceBase)
    
    def test_no_instance_from_interface_level_1(self):
        @interface
        class Level_1_interface(InterfaceBase): ...
        self.assertRaises(Exception, Level_1_interface)
    
    def test_no_instance_from_interface_level_2(self):
        @interface
        class Level_1_interface(InterfaceBase): ...
        @interface
        class Level_2_interface(Level_1_interface): ...
        
        self.assertRaises(Exception, Level_2_interface)
    
    def test_no_instance_from_interface_level_3(self):
        @interface
        class Level_1_interface(InterfaceBase): ...
        @interface
        class Level_2_interface(Level_1_interface): ...
        @interface
        class Level_3_interface(Level_2_interface): ...
        
        self.assertRaises(Exception, Level_3_interface)


if __name__ == "__main__":
    unittest.main()
