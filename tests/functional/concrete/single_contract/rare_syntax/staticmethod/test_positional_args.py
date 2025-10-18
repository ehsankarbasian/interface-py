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


if __name__ == "__main__":
    unittest.main()
