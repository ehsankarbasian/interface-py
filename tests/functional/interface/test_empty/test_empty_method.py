import unittest

import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent.parent.resolve()
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from interface_py import interface
from tests.functional.interface.test_helpers import SourceLoaderTestCase


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


    def test_empty_pass_exec_method(self):
        class_name = "MyInterface"

        lines = [f"class {class_name}:"]
        lines.append(f"    def my_method(self): pass")

        src = "\n".join(lines)
        global_vars = {}
        local_vars = {}
        exec(src, global_vars, local_vars)
        cls = local_vars[class_name]
        cls = interface(cls)
    
    
    def test_empty_ellipsis_exec_method(self):
        class_name = "MyInterface"

        lines = [f"class {class_name}:"]
        lines.append(f"    def my_method(self): ...")

        src = "\n".join(lines)
        global_vars = {}
        local_vars = {}
        exec(src, global_vars, local_vars)
        cls = local_vars[class_name]
        cls = interface(cls)


if __name__ == "__main__":
    unittest.main()
