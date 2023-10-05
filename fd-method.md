---
layout : default
use_math : true
---

# A look at the finite difference method

The finite difference method is a method that we can use to approximate derivatives. In fact, in many precalculus classes, this is introduced via the equation,

$$
f^{\prime}(x_o) = \lim_{h \rightarrow 0} \frac{f(x_o+h) - f(x_o)}{h}
$$

However, computers cannot understand what the limit of $h \rightarrow 0$ means. In other words, a computer cannot reach 0; it will always get to a number that is infinitesimally small yet not 0. So what do we do? Well, we can take a look at the Taylor series expansion of $f(x_o+h)$

$$
f(x_o+h) = f(x_o) + f^{(1)}(x_o)h + \frac{1}{2!}f^{(2)}(x_o)h^2 \\
               +\frac{1}{3!}f^{(3)}(x_o)h^3+...+ \frac{1}{n!}f^{(n)}(x_o)h^n+R_n(x)
$$

Here, $n$ is an arbitrary number for the total number of derivatives we include in the expansion, and the superscript in parentheses, $f^{(n)}$, represents the order of the derivative with respect to $x$ for the function. $R_n$ is the remainder term denoting the difference between the true equation and the approximated expansion. This is similar to the [Big-O notation](https://en.wikipedia.org/wiki/Big_O_notation) as it looks at the local truncation error and we will start using the Big-O notation from here on. If we then truncate the expansion to the first term we get,

$$
f(x_o+h) = f(x_o) + f^{(1)}(x_o)h + O(h)
$$

Re-arranging the equation then gives,

$$
f^{(1)}(x_o) = f^{\prime}(x_o) = \frac{f(x_o+h) - f(x_o)}{h} + O(h)
$$

Which is similar to equation **insert equation number** without the limit. The equation above is an approximation of the first derivative truncated to the first term and the error scales linearly as denoted by $O(h)$.

## Difference between forward, backward, and central FD approaches

Here, I want to explore the slight differences between the forward, backward, and central finite difference methods.

### Forward difference

This is actually the same equation as what we were looking at previously,

$$
f^{\prime}(x_o) = \frac{f(x_o+h) - f(x_o)}{h} + O(h)
$$

With linearly scaling error as we have already seen.

### Backward difference

The backward FD equation is similar to the forward difference,

$$
f^{\prime}(x_o) = \frac{f(x_o) - f(x_o-h)}{h} + O(h)
$$

The difference between the two comes from understanding the Taylor series expansion of $f(x_o-h)$ vs. $f(x_o+h)$. If we look at the generalized equation for a Taylor series,

$$
f(x) = \sum_{n=0}^{\infty} \frac{1}{n!}(x-a)^{n}\frac{d^{(n)}}{dx^{(n)}}f(a)
$$

Resulting in the following equation for the backward difference up to second order,

$$
\begin{align*}
f(x_o-h) \approx 
    &\frac{1}{0!}(x_o-h-x_o))^0 \frac{d^0}{dx^0} f(x_o) \\
    &+ \frac{1}{1!}(x_o-h-x_o)^1 \frac{d^1}{dx^1} f(x_o) \\
    &+ \frac{1}{2!}(x_o-h-x_o)^2 \frac{d^2}{dx^2} f(x_o) \\
\end{align*}
$$

We see that the $x_o$ terms on the right-hand side cancel each other out and after reducing terms we get,

$$
f(x_o-h) \approx (-h)^0 f(x_o) + (-h)^1 f^{\prime}(x_o) + (-h)^2 f^{\prime\prime}
$$

We can see that any linear terms will now carry a ($-$) sign in the expression and all quadratic terms remain positive. So what's the point of all this? Well we are about to see that.

### Central difference

The central finite difference method is a combination of the forward and backward difference methods. Without the specifics on how we get the equations, the central finite difference equation is,

$$
f^{\prime}(x_o) = \frac{f(x_o+h)-f(x_o-h)}{2h} + O(h^2)
$$

And that is the equation. But, what is the big deal? Well, if look at the last term in the equation you will notice that the error now depends quadratically on the step size, $O(h^2)$, thereby increasing the accuracy of the approximated derivative that we calculate. Now I will show you how this comes to be. The first thing to consider are the Taylor series expansions for $f(x_o+h)$ and $f(x_o-h)$,

$$
\begin{align*}
    f(x_o+h) = &f(x_o) + f^{(1)}(x_o)h + \frac{1}{2}f^{(2)}(x_o)h^2
               +\frac{1}{6}f^{(3)}(x_o)h^3 +O(h^3) \\
    f(x_o-h) = &f(x_o) - f^{(1)}(x_o)h + \frac{1}{2}f^{(2)}(x_o)h^2 
               -\frac{1}{6}f^{(3)}(x_o)h^3+O(h^3)
\end{align*}
$$

And taking the difference of the equations gives,

$$
f(x_o+h) - f(x_o-h) = 2f^{(1)}(x_o)h + \frac{1}{3}f^{(3)}(x_o)h^3+O(h^3)
$$

What we now see is that the even terms will cancel off and the odd terms will remain. As such, in order to have the equaion only depend on the first derivative we must truncate to the second order giving,

$$
f(x_o+h) - f(x_o-h) = 2f^{(1)}(x_o)h + O(h^2)
$$

With some re-arranging we get equation **insert equation number here**. So, by including extra points in the finite difference equation we can decrease the error in our approximation. With 2 points we get an error of $O(h^2)$, 3 points will have $O(h^3)$, etc. Just as a proof I will show what happens when we want to approximate the derivative with a [five-point stencil](https://en.wikipedia.org/wiki/Five-point_stencil), which has the equation

$$
f^{\prime}(x_o) = \frac{-f(x_o+2h)+8f(x_o+h)-8f(x_o-h)+f(x_o-2h)}{12h} + O(h^4)
$$

We would have the following equations for the Taylor series expansion,

$$
\begin{align*}
    f(x_o+h) = &f(x_o) + f^{(1)}(x_o)h + \frac{1}{2}f^{(2)}(x_o)h^2 \\
               &+\frac{1}{6}f^{(3)}(x_o)h^3+\frac{1}{24}f^{(4)}(x_o)h^4+O(h^4) \\
    f(x_o-h) = &f(x_o) - f^{(1)}(x_o)h + \frac{1}{2}f^{(2)}(x_o)h^2 \\
               &-\frac{1}{6}f^{(3)}(x_o)h^3+\frac{1}{24}f^{(4)}(x_o)h^4+O(h^4) \\
    f(x_o+2h) = &f(x_o) + f^{(1)}(x_o)2h + \frac{1}{2}f^{(2)}(x_o)4h^2 \\
               &+\frac{1}{6}f^{(3)}(x_o)8h^3+\frac{1}{24}f^{(4)}(x_o)16h^4+O(h^4) \\
    f(x_o-2h) = &f(x_o) - f^{(1)}(x_o)2h + \frac{1}{2}f^{(2)}(x_o)4h^2 \\
               &-\frac{1}{6}f^{(3)}(x_o)8h^3+\frac{1}{24}f^{(4)}(x_o)16h^4+O(h^4) \\
\end{align*}
$$

We must eliminate the third ($h^3$) and fourth ($h^4$) order terms from the expansion using,

$$
8[f(x_o+h)-f(x_o-h)] - [f(x_o+2h)-f(x_o-2h)]
$$

I know this is the equation based on the pre-factors in the known equation for the five-point stencil. If you work out the algebra using the equation above, you will find that all third and fourth-order terms cancel out and you get the actual equation. So you may be asking yourself why I even mentioned any of this. We already have the equations using multi-point finite difference methods. Well, I will now explain this.

## Computing the FD coefficients

So if you are interested in finding the coefficients for the FD method using more than two points, such as the five-point stencil, you can look [here](https://en.wikipedia.org/wiki/Finite_difference_coefficient) for the coefficients up to eight points. But, something that you might notice as I did is that the step sizes **MUST** be consecutive, i.e. you can have $f(x_o\pm h)$, $f(x_o\pm 2h)$, $f(x_o\pm 3h)$, etc. However, if you have $f(x_o\pm h)$, and $f(x_o\pm 3h)$ you can no longer use the five-point stencil as the third and fourth order terms will not cancel out in the Taylor series expansion. I am a big believer of seeing is believing so I will show you. Let's construct the Taylor series expansions for $f(x_o\pm h)$, and $f(x_o\pm 3h)$,

$$
\begin{align*}
    f(x_o+h) = &f(x_o) + f^{(1)}(x_o)h + \frac{1}{2}f^{(2)}(x_o)h^2 \\
               &+\frac{1}{6}f^{(3)}(x_o)h^3+\frac{1}{24}f^{(4)}(x_o)h^4+O(h^4) \\
    f(x_o-h) = &f(x_o) - f^{(1)}(x_o)h + \frac{1}{2}f^{(2)}(x_o)h^2 \\
               &-\frac{1}{6}f^{(3)}(x_o)h^3+\frac{1}{24}f^{(4)}(x_o)h^4+O(h^4) \\
    f(x_o+3h) = &f(x_o) + f^{(1)}(x_o)3h + \frac{1}{2}f^{(2)}(x_o)9h^2 \\
               &+\frac{1}{6}f^{(3)}(x_o)27h^3+\frac{1}{24}f^{(4)}(x_o)81h^4+O(h^4) \\
    f(x_o-3h) = &f(x_o) - f^{(1)}(x_o)3h + \frac{1}{2}f^{(2)}(x_o)9h^2 \\
               &-\frac{1}{6}f^{(3)}(x_o)27h^3+\frac{1}{24}f^{(4)}(x_o)81h^4+O(h^4) \\
\end{align*}
$$

If we use the equation,

$$
8[f(x_o+h)-f(x_o-h)] - [f(x_o+3h)-f(x_o-3h)]
$$

We get,

$$
f^{(1)}(x_o)10h - \frac{1}{6}f^{(3)}(x_o)38h^3 + O(h^4)
$$

The even terms disappear as we subtract even functions. The odd functions are where things get tricky as they carry a sign change and we see that the third-order terms remain in the equation. This means that we cannot approximate the derivative with those pre-factor coefficients anymore and we have to re-calculate them for this specific use case. This is a very simple case and the pre-factors are $27$ and $-1$ for $f(x_o\pm h)$ and $f(x_o\pm 3h)$, respectively. I calculated these by looking at the non-common pre-factor, ignoring the 1/6, for the third order term and I will get 54. The equation to approximate the first derivative is then,

$$
f^{\prime}(x_o) = \frac{-f(x_o+3h)+27f(x_o+h)-27f(x_o-h)+f(x_o-3h)}{48h} + O(h^4)
$$

Once you go into evaluating the coefficients for a six-point FD method, the situation becomes more complicated and requires the help of a computer program. So, I made a small Python script that I implemented into my library called [VibrAv](https://github.com/herbertludowieg/vibrav) and will share it below.

```python
Fancy python code goes here
```

Here I will put fancy text on how to compute the FD coefficients as seen on [here](https://en.wikipedia.org/wiki/Finite_difference_coefficient).
