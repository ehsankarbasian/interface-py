import unittest

import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent.parent.resolve()
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from tests.functional.interface.test_helpers import SourceLoaderTestCase


class InterfaceCanDefineEmptyContractTestCase(SourceLoaderTestCase):
    
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
    
    
    def test_empty_ellipsis_property(self):
        
        fake_source = '''
            from src.interface_py import interface
            
            @interface
            class MyInterface:
                
                @property
                def foo(self): ...
        '''
        
        self.load_interface_from_source(fake_source, "MyInterface")
    
    
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
