import os
import sys
import unittest
import importlib.util
from pathlib import Path


def load_all_tests(test_root: Path) -> unittest.TestSuite:
    project_root = test_root.parent
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    for root, dirs, files in os.walk(test_root):
        for exclude in ["benchmark", "__pycache__", 'scripts']:
            if exclude in dirs:
                dirs.remove(exclude)

        for file in files:
            if not file.endswith(".py"):
                continue
            if file in {"setup.py", "__init__.py"}:
                continue

            file_path = Path(root) / file
            relative_parts = file_path.relative_to(project_root).with_suffix("").parts
            module_name = ".".join(relative_parts)

            try:
                spec = importlib.util.spec_from_file_location(module_name, file_path)
                if spec and spec.loader:
                    module = importlib.util.module_from_spec(spec)
                    sys.modules[module_name] = module
                    spec.loader.exec_module(module)

                    suite.addTests(loader.loadTestsFromModule(module))
            except Exception as error:
                print(f"[WARN] Failed to import {file_path}: {error}")

    return suite


if __name__ == "__main__":
    try:
        project_root = Path(__file__).resolve().parent.parent.parent
    except NameError:
        project_root = Path.cwd().resolve().parent.parent
    
    test_root = project_root / "test"

    if len(sys.argv) > 1:
        arg_path = Path(sys.argv[1])
        if arg_path.exists():
            test_root = arg_path

    suite = load_all_tests(test_root)
    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(suite)
