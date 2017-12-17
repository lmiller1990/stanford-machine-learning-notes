1. Suppose you have m = 4 students in a class with a mid and final exam. Here are there results:

midterm | mid^2 | final
89 | 7961 | 96
72 | 5184 | 74
94 | 8836 | 87
69 | 4761 | 78

What is the normalize feature for dataset three, x1? Use (max-mid range toe scale feature).

The range of x1 = 94 - 69 = 25.
Average is 81.

So the scaled feature is:

(max - min) / av
(94 - 81) / 25 = 0.52.

For mid^2 it would be:

av = (8836 + 5184 + 7961 + 4761) / 4 = 6525
max - min = (8836 - 4761) = 4075

4075 / 6525 = 0.65.

2. You run grad desc for 15 iterations. A is increasing. What seems likely?

a is too large, it is overshooting. Use a smaller a value.

3. You have m=23 training examples, and n=5 features. What are n and m for theta = inv(X_trans X) * X_trans y?

X = 23x6
theta = 6x1
y = 23x1

Remember add all one feature for the intercept term, x0.

4. Dataset with m=100000 examples and n = 200000 features. You want to use multivariate linear regression to fit theta to the data. Grad desc or normal equation?

We should use grad desc. The matrices are far too large to invert, and will compute slowly.

5. Why use feature scaling?

So grad desc can get closer to converging with less iterations.
