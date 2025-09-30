import math
import time
import itertools
from memory_profiler import memory_usage
import matplotlib.pyplot as plt

import pathlib
import sys
path = str(pathlib.Path(__file__).parent.parent.parent.absolute())
sys.path.append(path)

from interface import interface, concrete, InterfaceBase
from abc import ABC, abstractmethod

# interactive mode on so figures can be shown non-blocking
plt.ion()


def run_and_collect(label, fn, n=1, interval=0.01):
    start = time.perf_counter()
    for _ in range(n):
        fn()
    dur = time.perf_counter() - start

    def wrapper():
        for _ in range(n):
            fn()

    mem_samples = memory_usage(wrapper, interval=interval, timeout=None)
    peak = max(mem_samples) - min(mem_samples) if mem_samples else 0.0
    
    print(f"{label:50s}: {dur:.4f} sec for {n} runs, +{peak:.4f} MiB peak memory")

    return {
        "label": label,
        "dur": dur,
        "mem": mem_samples,
        "peak": peak,
        "n": n,
        "interval": interval,
    }

def plot_group(results, group_title, cols=2, figsize_per_subplot=(6,3)):
    """Plot a list of result dicts (from run_and_collect) into one figure with subplots."""
    import math
    import matplotlib.pyplot as plt

    k = len(results)
    cols = max(1, cols)
    rows = math.ceil(k / cols)
    fig_w = figsize_per_subplot[0] * cols
    fig_h = figsize_per_subplot[1] * rows
    fig, axes = plt.subplots(rows, cols, figsize=(fig_w, fig_h), constrained_layout=True)
    
    # flatten axes list
    if isinstance(axes, (list, tuple)):
        axes_list = list(axes)
    else:
        axes_list = list(axes.flat)
    
    for i, res in enumerate(results):
        ax = axes_list[i]
        mem = res["mem"]
        if not mem:
            ax.text(0.5, 0.5, "no samples", ha="center", va="center")
        else:
            x = [idx * res["interval"] for idx in range(len(mem))]
            ax.plot(x, mem, lw=1)
        
        ax.set_title(f"{res['label']}\n{res['dur']:.3f}s, +{res['peak']:.3f} MiB")
        ax.set_xlabel("time (s)")
        ax.set_ylabel("memory (MiB)")
        
        for spine in ax.spines.values():
            spine.set_visible(True)
            spine.set_linewidth(1.5)
            spine.set_edgecolor("black")

    # hide unused axes
    for j in range(k, rows * cols):
        axes_list[j].axis("off")
    
    fig.suptitle(group_title)

    # ensure nothing overlaps, fully contained in own subplot
    plt.tight_layout()
    
    try:
        fig.canvas.manager.set_window_title(group_title)
    except Exception:
        pass
    
    plt.show(block=False)
    plt.pause(0.1)
    return fig


@interface
class FooInterface(InterfaceBase):
    x: int
    def do(self): ...
    @staticmethod
    def s(): ...
    @property
    def y(self): ...


@concrete
class ConcreteFooInterface(FooInterface):
    x: int = 10
    def do(self): return 42
    @staticmethod
    def s(): return "ok"
    @property
    def y(self): return "y"


class AbstractFoo(ABC):
    @abstractmethod
    def do(self): ...
    @abstractmethod
    def s(self): ...
    @property
    @abstractmethod
    def y(self): ...

class ConcreteFooABC(AbstractFoo):
    def do(self): return 42
    def s(self): return "ok"
    @property
    def y(self): return "y"


def make_interface_class():
    @interface
    class FakeInterface(InterfaceBase):
        a: int
        def f(self): ...
    return FakeInterface

def make_concrete_class():
    @concrete
    class FakeConcrete(ConcreteFooInterface):
        pass
    return FakeConcrete

def make_abc_class():
    class FakeABC(ABC):
        @abstractmethod
        def f(self): ...
    return FakeABC

def make_abc_impl():
    class ConcreteFakeABC(make_abc_class()):
        def f(self): return 1
    return ConcreteFakeABC


_unique_counter = itertools.count(0)

def make_big_interface(num_fields=100, num_methods=100, with_annotations=True):
    index = next(_unique_counter)
    cls_name = f"BigInterface_{num_fields}f_{num_methods}m_{index}"

    lines = [f"class {cls_name}(InterfaceBase):"]
    for i in range(num_fields):
        if with_annotations:
            if i % 2 == 0:
                lines.append(f"    field_{i}: int")
            else:
                lines.append(f"    field_{i}: int = ...")
        else:
            lines.append(f"    field_{i} = ...")

    for j in range(num_methods):
        lines.append(f"    def method_{j}(self): ...")

    src = "\n".join(lines)
    g = {"InterfaceBase": InterfaceBase}
    local_vars = {}
    exec(src, g, local_vars)
    cls = local_vars[cls_name]
    cls = interface(cls)
    return cls


def make_big_abc(num_fields=0, num_methods=100, with_annotations=True):
    index = next(_unique_counter)
    cls_name = f"BigABC_{num_fields}f_{num_methods}m_{index}"

    lines = [f"class {cls_name}(ABC):"]
    for j in range(num_methods):
        lines.append(f"    @abstractmethod")
        lines.append(f"    def method_{j}(self): ...")

    src = "\n".join(lines)
    g = {"ABC": ABC, "abstractmethod": abstractmethod}
    local_vars = {}
    exec(src, g, local_vars)
    cls = local_vars[cls_name]
    return cls


def make_big_concrete_from_interface(iface_cls):
    index = next(_unique_counter)
    cls_name = f"ConcreteImpl_{iface_cls.__name__}_{index}"
    lines = [f"class {cls_name}({iface_cls.__name__}):"]

    annotations = getattr(iface_cls, "__annotations__", {})
    ellipsis_fields = [k for k, v in iface_cls.__dict__.items() if v is Ellipsis and not k.startswith("__")]
    field_names = set(annotations.keys()) | set(ellipsis_fields)

    for field_name in sorted(field_names):
        lines.append(f"    {field_name} = 1")

    method_names = [k for k, v in iface_cls.__dict__.items() if callable(v) and not k.startswith("__")]
    for m in sorted(method_names):
        if m.startswith("method_") or m.startswith("f") or m in ("do",):
            lines.append(f"    def {m}(self):")
            lines.append(f"        return 1")

    src = "\n".join(lines)
    g = {iface_cls.__name__: iface_cls}
    local_vars = {}
    exec(src, g, local_vars)
    cls = local_vars[cls_name]
    cls = concrete(cls)
    return cls


def make_big_abc_impl(abc_cls):
    index = next(_unique_counter)
    cls_name = f"ABCImpl_{abc_cls.__name__}_{index}"
    lines = [f"class {cls_name}({abc_cls.__name__}):"]
    method_names = [k for k, v in abc_cls.__dict__.items() if callable(v) and not k.startswith("__")]
    
    for m in method_names:
        lines.append(f"    def {m}(self):")
        lines.append(f"        return 1")
    
    src = "\n".join(lines)
    g = {abc_cls.__name__: abc_cls}
    local_vars = {}
    exec(src, g, local_vars)
    cls = local_vars[cls_name]
    return cls


if __name__ == "__main__":
    # small quick baseline
    N = 10000
    small_results = []
    small_results.append(run_and_collect("Interface definition (small)", make_interface_class, n=N))
    small_results.append(run_and_collect("Concrete definition (small)", make_concrete_class, n=N))
    small_results.append(run_and_collect("ABC definition (small)", make_abc_class, n=N))
    small_results.append(run_and_collect("ABC implementation (small)", make_abc_impl, n=N))

    plot_group(small_results, f"Quick baseline: {N} iterations - memory timelines", cols=2)

    print("\n\n------ Large-class benchmarks (time + memory) ------\n")

    sizes = [
        (50, 50, 200, 'Small'),
        (200, 200, 200, 'Medium'),
        (800, 800, 200, 'Large'),
    ]

    for num_fields, num_methods, iterations, size_name in sizes:
        group_results = []
        group_results.append(run_and_collect(f"Interface {num_fields} fields / {num_methods} methods", 
                                            lambda: make_big_interface(num_fields, num_methods, True),
                                            n=iterations))
        group_results.append(run_and_collect(f"Interface {num_fields}f/{num_methods}m -> concrete",
                                            lambda: make_big_concrete_from_interface(make_big_interface(num_fields, num_methods, True)),
                                            n=iterations))
        group_results.append(run_and_collect(f"ABC {num_methods} methods",
                                            lambda: make_big_abc(0, num_methods, True),
                                            n=iterations))
        group_results.append(run_and_collect(f"ABC {num_methods} -> implementation",
                                            lambda: make_big_abc_impl(make_big_abc(0, num_methods, True)),
                                            n=iterations))
        print()

        plot_group(group_results, f"{size_name} class suite: {num_fields} fields & {num_methods} methods - {iterations} iterations", cols=2)

    print("\nDone. All figures are opened (non-blocking).")
    input("Press Enter to finish and close all plots...")
