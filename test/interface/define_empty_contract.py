import unittest
from unittest import TestCase

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.absolute())
sys.path.append(path)

from interface import interface


class InterfaceCanDefineEmptyContractTestCase(TestCase):
    
    def test_empty_pass_method(self):
        
        @interface
        class MyInterface:
            
            def foo(self):
                pass
    
    
    def test_empty_pass_classmethod(self):
        
        @interface
        class MyInterface:
            
            @classmethod
            def foo(cls):
                pass
    
    
    def test_empty_pass_staticmethod(self):
        
        @interface
        class MyInterface:
            
            @staticmethod
            def foo():
                pass
    
    
    def test_empty_pass_property(self):
        
        @interface
        class MyInterface:
            
            @property
            def foo(self):
                pass
    
    
    def test_empty_three_dots_method(self):
        
        @interface
        class MyInterface:
            
            def foo(self): ...
    

    def test_empty_three_dots_classmethod(self):
        
        @interface
        class MyInterface:
            
            @classmethod
            def foo(cls): ...
    

    def test_empty_three_dots_staticmethod(self):
        
        @interface
        class MyInterface:
            
            @staticmethod
            def foo(): ...
    

    def test_empty_three_dots_property(self):
        
        @interface
        class MyInterface:
            
            @property
            def foo(self): ...
    

    def test_empty_docstring_method(self):
        
        @interface
        class MyInterface:
            
            def foo(self):
                """ Explanation """


    def test_empty_docstring_classmethod(self):
        
        @interface
        class MyInterface:
            
            @classmethod
            def foo(cls):
                """ Explanation """


    def test_empty_docstring_staticmethod(self):
        
        @interface
        class MyInterface:
            
            @staticmethod
            def foo():
                """ Explanation """


    def test_empty_docstring_property(self):
        
        @interface
        class MyInterface:
            
            @property
            def foo(self):
                """ Explanation """


if __name__ == "__main__":
    unittest.main()
