import unittest

import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).parent.parent.parent.resolve()
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.interface_py import interface
from test.interface.test_helpers import SourceLoaderTestCase


class InterfaceCanDefineEmptyContractTestCase(SourceLoaderTestCase):
    
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
            from src.interface_py import interface
            
            @interface
            class MyInterface:
                
                @property
                def foo(self):
                    pass
        '''
        
        self.load_interface_from_source(fake_source, "MyInterface")
    
    
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
            from src.interface_py import interface
            
            @interface
            class MyInterface:
                
                @property
                def foo(self): ...
        '''
        
        self.load_interface_from_source(fake_source, "MyInterface")
    

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
            from src.interface_py import interface
        
            @interface
            class MyInterface:
                
                @property
                def foo(self):
                    """ Explanation """
        '''
        
        self.load_interface_from_source(fake_source, "MyInterface")


if __name__ == "__main__":
    unittest.main()
