import matplotlib.pyplot as plt

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.absolute())
sys.path.append(path)

from plot_tools import plot_group
from class_generator import make_interface_class, make_concrete_class, make_abc_class, make_abc_impl
from big_class_generator import make_big_interface, make_big_abc, make_big_concrete_from_interface, make_big_abc_impl
from runner import run_with_and_without_gc


# interactive mode on so figures can be shown non-blocking
plt.ion()


if __name__ == "__main__":
    # small quick baseline
    N = 10000
    small_results = []
    for result in run_with_and_without_gc("Interface definition (small)", make_interface_class, n=N):
        small_results.append(result)
    for result in run_with_and_without_gc("Concrete definition (small)", make_concrete_class, n=N):
        small_results.append(result)
    for result in run_with_and_without_gc("ABC definition (small)", make_abc_class, n=N):
        small_results.append(result)
    for result in run_with_and_without_gc("ABC implementation (small)", make_abc_impl, n=N):
        small_results.append(result)

    plot_group(small_results, f"Quick baseline: {N} iterations - memory timelines", cols=2)


    print("\n\n------ Large-class benchmarks (time + memory) ------\n")

    sizes = [
        (50, 50, 200, 'Small'),
        (200, 200, 200, 'Medium'),
        (800, 800, 200, 'Large'),
        (4000, 4000, 200, 'Extra Large'),
    ]

    for num_fields, num_methods, iterations, size_name in sizes:
        group_results = []
        
        for result in run_with_and_without_gc(f"Interface {num_fields} fields / {num_methods} methods", 
                                            lambda: make_big_interface(num_fields, num_methods, True),
                                            n=iterations):
            group_results.append(result)
        for result in run_with_and_without_gc(f"Interface {num_fields} fields / {num_methods} methods -> concrete",
                                            lambda: make_big_concrete_from_interface(make_big_interface(num_fields, num_methods, True)),
                                            n=iterations):
            group_results.append(result)
        for result in run_with_and_without_gc(f"ABC {num_methods} methods",
                                            lambda: make_big_abc(0, num_methods, True),
                                            n=iterations):
            group_results.append(result)
        for result in run_with_and_without_gc(f"ABC {num_methods} -> implementation",
                                            lambda: make_big_abc_impl(make_big_abc(0, num_methods, True)),
                                            n=iterations):
            group_results.append(result)

        print()

        plot_group(group_results, f"{size_name} class suite: {num_fields} fields & {num_methods} methods - {iterations} iterations", cols=2)

    print("\nDone. All figures are opened (non-blocking).")
    input("Press Enter to finish and close all plots...")
