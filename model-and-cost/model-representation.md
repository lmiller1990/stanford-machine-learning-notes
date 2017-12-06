# Model Representation
Predict the price of a house given some data. 

- Regression problem - predicting real valued output
- Supervised learning
- We have a *training set* 

Notation: 
m = number of training examples
x = input variable / feature
y = output variable / target

(x, y) = one training example
x^i, y^i = ith traning example

Training set -> learning algo -> hypothesis

size of house (x) -> h -> estimated price
_h is a function that maps from x's to y's_

# Cost Function

Choose 0o, 01, so that h(x) is close to y for training examples (x, y)

We need to choose a good cost function. Square error function is generally a good choice.
