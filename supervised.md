## Machine learning algorithms

- Supervised learning
- Unsupervised learning

Others:
- Reinforcement learning, recommender systems

### Supervised Learning or Regression problem
- Predict continuous valued output (price)
- Used for classification problems
- Discrete valued output (0 or 1)
- Can be more than two values

Example: is cancer benign or malignant?
Features:
- Age
- Tumor size
- Clump thickness
- Uniformity of cell size
- Uniformity of cell shape

Can have infinite features - using such algos like a Support Vector Machine (SVM).

Supervised learning for every example in the dataset, we are told the "correct" answer - eg, is the cancer benign or malignant

### Regression vs Classification
Regression - to predict the output value using trained data. Predict continuous valued output. Discrete values (1, 2, 3...) as inputs.

We are trying to predict results withint a continuous output, meaning we are mapping input variables to some continuous function.

Classification - group the output in a class. Continuous values (222.45..) for inputs.

We are trying to predict results in a discrete outputs/categories (such as is or is not benign, is or is not hacked).

#### Classification examples
- given some input features, predict whether a breast cancer is benign or malignant
- classify an image as containing dogs or cats
- predict whether email is spam or not
- given a patient with a tumor, predict whether the tumor is benign or malignant

Some classification algorithms:
- decision tree
- logistic regression
- naive bayes
- K nearest neighbors

#### Regression examples
- given a house size, predict the value
- given the number of people in a family, predict the number of rooms in a house
- given a picture of a person, predict their age

Some classification algorithms:
- linear regression
- random forest regression tree

### Quiz:

Problem 1: You want software to predict how many items will sell over the next three months.
Problem 2: You want software to decide if a user account has been hacked or compromised.

Problem 1 - Discrete - so it's a regression problem. 
Problem 2 - Grouping output into categories - classification problem.

### Summary

In a regression problem, we are predicting some results within a continuous output. This means we are mapping input variables to some continuous function. In a classification problem, we are mapping some input variables to a discrete output.

Example: Given some data about the size of a house, predict the price. The output is a continuous function, so it is a regression problem.

Let's take another angle:

Given an asking price, does the house sell? Now we are classifying the house based on two discrete categories - yes or no. It is now a classification problem.

