import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('casablanca_housing.csv')
data.head()
# #Prediction du MEDV

# Prepare the data
X = data[['RM', 'LSTAT', 'PTRATIO']]  # Features
y = data['MEDV']  # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

#Example prediction
#Create a new data point for prediction
new_data_point = pd.DataFrame({'RM': [6.5], 'LSTAT': [10], 'PTRATIO': 18})
#Predict the MEDV for the new data point
predicted_medv = model.predict(new_data_point)
print(f'Predicted MEDV for the new data point: {predicted_medv[0]}')
# #Pairplots appropriés 

# Create the pairplot
sns.pairplot(data[['RM', 'LSTAT', 'PTRATIO', 'MEDV']])
plt.show()
