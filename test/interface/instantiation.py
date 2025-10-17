import unittest
from unittest import TestCase

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.absolute())
sys.path.append(path)

from interface_py import interface


class InterfaceInstantiationTestCase(TestCase):
    
    def setUp(self):
        
        @interface
        class Level_1_Interface_dot: ...
        @interface
        class Level_2_Interface_dot(Level_1_Interface_dot): ...
        @interface
        class Level_3_Interface_dot(Level_2_Interface_dot): ...
        
        self.Level_1_Interface_dot = Level_1_Interface_dot
        self.Level_2_Interface_dot = Level_2_Interface_dot
        self.Level_3_Interface_dot = Level_3_Interface_dot
        
        @interface
        class Level_1_Interface_pass: pass
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
        self.assertRaises(TypeError, self.Level_1_Interface_dot)
        self.assertRaises(TypeError, self.Level_1_Interface_pass)
        
        self.assertRaises(TypeError, self.Level_2_Interface_dot)
        self.assertRaises(TypeError, self.Level_2_Interface_pass)
        
        self.assertRaises(TypeError, self.Level_3_Interface_dot)
        self.assertRaises(TypeError, self.Level_3_Interface_pass)
    
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


if __name__ == "__main__":
    unittest.main()
