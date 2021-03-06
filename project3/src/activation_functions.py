import numpy as np

''' File contains all operations on activation functions'''

def sigmoid(x):
	''' Sigmoid activation function'''
	return 1.0/(1.0 + np.exp(-x))

def ReLU(x):
	''' ReLU activation function'''
	return np.maximum(0,x)

def leaky_ReLU(x):
	''' Leaky ReLU activation function'''
	return np.where(x<=0, 0.001*x, x)

def softmax(x):
	''' Softmax activation function'''
	exp_term = np.exp(x)
	return exp_term / np.sum(exp_term, axis=1, keepdims=True)

def set_activation_function(x, activation_function):
	''' Function returns an activation function according to the choice'''
	if(activation_function =="softmax"):
		return softmax(x)
	elif(activation_function =="sigmoid"):
		return sigmoid(x)
	elif(activation_function =="relu"):
		return ReLU(x)
	elif(activation_function =="leaky relu"):
		return leaky_ReLU(x)
	elif(activation_function =="tanh"):
		return np.tanh(x)
	elif(activation_function =="linear"):
		return x
	elif(activation_function =="binary step"):
		return np.heaviside(x, 0)

def set_activation_function_deriv(x, activation_function):
	''' Function returns a derivative of an activation 
	function according to the choice'''
	if(activation_function =="softmax"):
		return softmax(x)*(1-softmax(x))
	elif(activation_function =="sigmoid"):
		return sigmoid(x)*(1-sigmoid(x))
	elif(activation_function =="relu"):
		return np.heaviside(x, 0)
	elif(activation_function == "leaky relu"):
		return np.where(x<=0, 0.001, 1)
	elif(activation_function =="tanh"):
		return 1-np.tanh(x)**2
	elif(activation_function =="linear"):
		return 1
	elif(activation_function =="binary step"):
		return np.where(x==0, nan, 0)