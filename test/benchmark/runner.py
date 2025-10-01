import gc
import time
from memory_profiler import memory_usage


def _run_and_collect(label, fn, n=1, interval=0.01):
    start = time.perf_counter()
    for _ in range(n):
        fn()
    dur = time.perf_counter() - start

    def wrapper():
        for _ in range(n):
            fn()

    mem_samples = memory_usage(wrapper, interval=interval, timeout=None)
    peak = max(mem_samples) - min(mem_samples) if mem_samples else 0.0
    
    print(f"{label:45s}: {dur:.4f} sec for {n} runs, +{peak:.4f} MiB peak memory")

    return {
        "label": label,
        "dur": dur,
        "mem": mem_samples,
        "peak": peak,
        "n": n,
        "interval": interval,
    }


def run_with_and_without_gc(label, fn, n=1, interval=0.01):
    results = []

    gc.enable()
    res_gc_on = _run_and_collect(label + " [GC ON]", fn, n=n, interval=interval)
    results.append(res_gc_on)

    gc.disable()
    res_gc_off = _run_and_collect(label + " [GC OFF]", fn, n=n, interval=interval)
    results.append(res_gc_off)
    gc.enable()
    
    return results
