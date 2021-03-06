#Neural network that predicts the price of a house.

import numpy as np
from tensorflow import keras

# GRADED FUNCTION: house_model
def house_model(y_new):
	#xs represents number of bedrooms in a house
    xs = np.array([1, 2, 3, 4, 5, 6], dtype=float)
	
	#ys represents cost of house according to number of bedrooms the house has - i.e. a 1 bedroom house costs 100k, a 2 bedroom house costs 150k etc.
    ys = np.array([1.0, 1.5, 2.0, 2.5, 3.0, 3.5], dtype=float)
    
	#model designing
    #Sequential - sequence of layers in NN
    model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
    #compiling model with optimization and loss functions
    model.compile(optimizer='sgd', loss='mean_squared_error')
    # model fitting - fitting training data to training labels so that it can figure out a relationship between them
    # and the model can be used for future predictions
    model.fit(xs, ys, epochs=500)
    return model.predict(y_new)[0]

#Predict price of house with 7 bedrooms	
prediction = house_model([7.0])
print(prediction)