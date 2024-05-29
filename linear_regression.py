import numpy as np 

#Create randomly generated data set
m=100 #no of samples
X = 2*np.random.rand(m,1) # column vector
y = 4+3*X + np.random.randn(m,1)

#Train the model using sklearn
from sklearn.preprocessing import add_dummy_feature
X_b = add_dummy_feature(X) #add another column x0=1 to each instance
theta = np.linalg.inv(X_b.T@X_b)@(X_b.T@y)
print(theta)