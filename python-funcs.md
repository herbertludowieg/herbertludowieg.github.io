---
layout: default
---

# Helpful Python functions

## Alignment of y-axis for plots

Here will go a nice example of when this thing is actually useful.

```python
def align_y_axis(ax1, ax2):
    axes = (ax1, ax2)
    extrema = [ax.get_ylim() for ax in axes]
    tops = [extr[1] / (extr[1] - extr[0]) for extr in extrema
    if tops[0] > tops[1]:
        axes, extrema, tops = [list(reversed(l)) for l in (axes, extrema, tops)]
    tot_span = tops[1] + 1 - tops[0]
    b_new_t = extrema[0][0] + tot_span * (extrema[0][1] - extrema[0][0])
    t_new_b = extrema[1][1] - tot_span * (extrema[1][1] - extrema[1][0])
    axes[0].set_ylim(extrema[0][0], b_new_t)
    axes[1].set_ylim(t_new_b, extrema[1][1])
```

[Back to main page](index.md)
