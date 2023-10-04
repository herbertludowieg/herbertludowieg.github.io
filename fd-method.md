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

Here, $n$ is an arbitrary number for the total number of derivatives we include in the expansion, and the superscript in parentheses, $f^{(n)}$, represents the order of the derivative with respect to $x$ for the function. $R_n$ is the remainder term denoting the difference between the true equation and the approximated expansion, this is similar to the [Big-O notation](https://en.wikipedia.org/wiki/Big_O_notation) as it is looking at the local truncation error and we will start using the Big-O notation from here on. If we then truncate the expansion to the first term we get,

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
    f(x_o+h) = f(x_o) + f^{(1)}(x_o)h + \frac{1}{2}f^{(2)}(x_o)h^2
               +\frac{1}{6}f^{(3)}(x_o)h^3 +O(h^3) \\
    f(x_o-h) = f(x_o) - f^{(1)}(x_o)h + \frac{1}{2}f^{(2)}(x_o)h^2 
               -\frac{1}{6}f^{(3)}(x_o)h^3+O(h^3)
\end{align*}
$$

And taking the difference of the equations gives,

## Computing the FD coefficients

Here I will put fancy text on how to compute the FD coefficients as seen on [here](https://en.wikipedia.org/wiki/Finite_difference_coefficient).
