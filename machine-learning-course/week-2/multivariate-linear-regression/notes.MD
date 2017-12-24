# Multivariate linear regression

## Feature Scaling

Ideally, you can get better results and help gradient descent converge more quickly if you use feature scaling.

Concretely, say we have 

x1 = size (ft): range 0 - 2000
x2 = # rooms: range 1 - 5

A nice range is -1 < x < 1

So, we can instead say:

x1 = size / 2000
x2 = rooms / 5

Or, feature / max

## Mean Normalization

The above can be further improved by doing:

feature - average / max.

## Example
x1 = age in years. Houses between 30-50 yrs old. So,

x1 <- (rooms - 38) / 20

## Practise Question
You want to predict the price of a house. Your model is:
h(x) = theta0 + theta1 (size) + theta2 (sqrt(size))

Houses range from 0 - 1000 ft. You will implement by fitting this model:

h(x) = theta0 + theta1(x1) + theta2(x2)

with feature scaling. Which values are x1 and x2?

1. x1 = size, x2 = 32 sqrt(size)
2. x1 = 32(size), x2 = sqrt(size)
3. x1 = size/1000, x2 = sqrt(size)/32
4. x1 = size/32, x2 = sqrt(size)


When we do feature scaling, we can simply divide by the max. So feature/max.

Therefore the answer is 3. Since hte model is theta2(sqrt(size)), we need to divide by the max, which is scaled correctly, so it's sqrt(size)/32, where 32 is approx sqrt(1000), the max.

# Polynomial regression

We can improve our hypothesis in a few ways. One is combining several features, like length x width = area.

We can also change the bahavior or curve of the hypothesis function by using a quadratic, cubic, or squire root function, or another other form.

