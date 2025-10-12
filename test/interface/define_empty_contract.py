import unittest
from unittest import TestCase

import sys
from pathlib import Path
# find absolute project root
ROOT_PATH = Path(__file__).resolve().parents[2]
if str(ROOT_PATH) not in sys.path:
    sys.path.insert(0, str(ROOT_PATH))

from src import interface
from test.utils import load_interface_from_source


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
        
        fake_source = '''
            from src import interface
            
            @interface
            class MyInterface:
                
                @property
                def foo(self):
                    pass
        '''
        
        load_interface_from_source(fake_source, "MyInterface")
    
    
    def test_empty_ellipsis_method(self):
        
        @interface
        class MyInterface:
            
            def foo(self): ...
    

    def test_empty_ellipsis_classmethod(self):
        
        @interface
        class MyInterface:
            
            @classmethod
            def foo(cls): ...
    

    def test_empty_ellipsis_staticmethod(self):
        
        @interface
        class MyInterface:
            
            @staticmethod
            def foo(): ...
    

    def test_empty_ellipsis_property(self):
        
        fake_source = '''
            from src import interface
            
            @interface
            class MyInterface:
                
                @property
                def foo(self): ...
        '''
        
        load_interface_from_source(fake_source, "MyInterface")
    

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
        
        fake_source = '''
            from src import interface
        
            @interface
            class MyInterface:
                
                @property
                def foo(self):
                    """ Explanation """
        '''
        
        load_interface_from_source(fake_source, "MyInterface")


if __name__ == "__main__":
    unittest.main()
