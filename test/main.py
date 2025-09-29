import os
import sys
import unittest
import importlib.util


TEST_ROOT_DIR = "test"


if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    for root, dirs, files in os.walk(TEST_ROOT_DIR):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                
                spec = importlib.util.spec_from_file_location(file[:-3], file_path)
                if spec and spec.loader:
                    module = importlib.util.module_from_spec(spec)
                    sys.modules[file[:-3]] = module
                    try:
                        spec.loader.exec_module(module)
                        tests = loader.loadTestsFromModule(module)
                        suite.addTests(tests)
                    except Exception as e:
                        print(f"Failed to load {file_path}: {e}")

    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(suite)
