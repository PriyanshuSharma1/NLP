x = [1,2,3,4,5]
y = [2,4,6,8,10]
weight = 0
bias = 0
learning_rate = 0.1

for epoch in range(10):
    for i in range(len(x)):
        y_pred = x[i] * weight + bias
        error = y[i] - y_pred
        weight += learning_rate * error * x[i]
        bias += learning_rate * error
    print(f"Epoch {epoch+1}: weight = {weight}, bias = {bias}")
print(f"Final weight: {weight}, Final bias: {bias}")
# This code implements a simple linear regression model using gradient descent.
a = 7
print("calculating value for input a", a*weight + bias)