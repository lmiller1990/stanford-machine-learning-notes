function J = computeCost(X, y, theta)
%COMPUTECOST Compute cost for linear regression
%   J = COMPUTECOST(X, y, theta) computes the cost of using theta as the
%   parameter for linear regression to fit the data points in X and y

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta
%               You should set J to the cost.

prediction = X * theta;
diff = (prediction - y);

error = diff .^ 2;


s = 0;
for iter = 1:size(error);
  s = s + error(iter);
end


J = 1 / (2 * m) * s % sum(error);


%cost () {
%// x is array of housing sizes
%// y is housing prices
%// M is size of training set
%let sum = 0
%
%for (let i = 0; i < this.M; i++) {
%sum += Math.pow(this.hypothesis(this.x[i]) - this.y[i],  2)
%
%}
%
%return sum / (2 * this.M)


% =========================================================================

end
