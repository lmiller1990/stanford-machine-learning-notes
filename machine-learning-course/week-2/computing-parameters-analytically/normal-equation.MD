# Normal Equation

- Can be a more optimal way to solve for theta in gradient descent.
- Normal equation can solve analytically - no need to learn and iterate constnantly.
- For some quadratic cost function, how to you minimize?
- Take derivative wrt the param theta, and set to 0, then solve.
- Doing is this way means you do not need to bother with Feature Scaling.

# Equation

theta = inv(X_transpose X) * X_transpose y
In octave: pinv(X' * X) * X' * y

## Example
Say I have this data:

Age | height | weight
4   | 128    |  15
9   | 120    |  20
3   | 100    |  10

Model is: theta0 + theta1 (age) + theta2 (height)

X and y?

X = [
 [1, 4, 128],
 [1, 9, 120],
 [1, 3, 100]
]

y = [
 [15]
 [20]
 [10]
]

Remember, we add x0 = 1 for all training sets.

# When to use Grad Desc and Normal Equation

_m_ training examples, _n_ features.

Grad:
- need to choose learning rate alpha
- needs many iterations
- works for large values of _n_

Norm:
- don't need alpha
- don't need to iterate
- need to compute inv(X_transpose X), which is o(n^3)...slow.
- does not work well for large values of _n_ 

## What is a large n?

< 10000, can use normal equation.
Greater than that, maybe linear regression is a good choice.
