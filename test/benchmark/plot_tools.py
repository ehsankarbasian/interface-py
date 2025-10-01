
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
