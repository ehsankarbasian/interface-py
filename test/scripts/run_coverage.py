#!/usr/bin/env python3
import sys
from pathlib import Path
import unittest
from coverage import Coverage
import importlib.util

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
SCRIPT_MAIN = PROJECT_ROOT / "test" / "scripts" / "main.py"

# اضافه کردن مسیر پروژه به sys.path
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# import تابع load_all_tests از main.py
spec = importlib.util.spec_from_file_location("scripts.main", SCRIPT_MAIN)
module_main = importlib.util.module_from_spec(spec)
sys.modules["scripts.main"] = module_main
spec.loader.exec_module(module_main)

# حالا تابع load_all_tests در module_main موجود است
load_all_tests = module_main.load_all_tests

def main():
    test_root = PROJECT_ROOT / "test"

    cov = Coverage(source=[str(PROJECT_ROOT / "src")], omit=["*/test/*", "*/tests/*"])
    cov.start()

    print("\nRunning tests with coverage...\n")

    suite = load_all_tests(test_root)

    runner = unittest.TextTestRunner(verbosity=1)
    result = runner.run(suite)

    cov.stop()
    cov.save()

    print("\nGenerating coverage reports...\n")
    cov.report(show_missing=True)
    cov.html_report(directory=str(PROJECT_ROOT / "coverage_html"))

    print(f"\n✅ HTML coverage report generated at: {PROJECT_ROOT / 'coverage_html' / 'index.html'}")

    return 0 if result.wasSuccessful() else 1

if __name__ == "__main__":
    sys.exit(main())
