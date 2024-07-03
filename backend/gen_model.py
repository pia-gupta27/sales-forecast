import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
import math
import warnings
import pickle

warnings.simplefilter("ignore")

# Set seed for reproducibility
np.random.seed(0)

# Load the datasets
train_path = 'Train.csv'
test_path = 'Test.csv'

train = pd.read_csv(train_path)
test = pd.read_csv(test_path)

# Quick check of the data
train_info = train.info()
test_info = test.info()

train_info, test_info

# Missing Value Treatment for train
train['Outlet_Size'] = train['Outlet_Size'].fillna(train['Outlet_Size'].mode()[0])
train['Item_Weight'] = train['Item_Weight'].fillna(train['Item_Weight'].mean())

# Missing Value Treatment for test
test['Outlet_Size'] = test['Outlet_Size'].fillna(test['Outlet_Size'].mode()[0])
test['Item_Weight'] = test['Item_Weight'].fillna(test['Item_Weight'].mean())

# Function to detect outliers using the IQR method
def detect_outliers(df, feature):
    Q1 = df[feature].quantile(0.25)
    Q3 = df[feature].quantile(0.75)
    IQR = Q3 - Q1
    upper_limit = Q3 + 1.5 * IQR
    lower_limit = Q1 - 1.5 * IQR
    return upper_limit, lower_limit

# Removing outliers for 'Item_Visibility'
upper, lower = detect_outliers(train, "Item_Visibility")
train = train[(train['Item_Visibility'] > lower) & (train['Item_Visibility'] < upper)]
test = test[(test['Item_Visibility'] > lower) & (test['Item_Visibility'] < upper)]

# Removing outliers for 'Item_Outlet_Sales'
upper, lower = detect_outliers(train, "Item_Outlet_Sales")
train = train[(train['Item_Outlet_Sales'] > lower) & (train['Item_Outlet_Sales'] < upper)]

# Correcting the errors in the Item_Fat_Content column
item_fat_content_map = {
    'Low Fat': 'Low Fat',
    'low fat': 'Low Fat',
    'LF': 'Low Fat',
    'Regular': 'Regular',
    'reg': 'Regular'
}
train['Item_Fat_Content'] = train['Item_Fat_Content'].map(item_fat_content_map)
test['Item_Fat_Content'] = test['Item_Fat_Content'].map(item_fat_content_map)

# Getting the amount of established years in a new column and delete old column
train['Outlet_Age'] = 2023 - train['Outlet_Establishment_Year']
test['Outlet_Age'] = 2023 - test['Outlet_Establishment_Year']
del train['Outlet_Establishment_Year']
del test['Outlet_Establishment_Year']

# Encoding Outlet_Size
outlet_size_map = {'Small': 1, 'Medium': 2, 'High': 3}
train['Outlet_Size'] = train['Outlet_Size'].map(outlet_size_map).astype(int)
test['Outlet_Size'] = test['Outlet_Size'].map(outlet_size_map).astype(int)

# Encoding Outlet_Location_Type by getting the last character and converting to int type
train['Outlet_Location_Type'] = train['Outlet_Location_Type'].str[-1].astype(int)
test['Outlet_Location_Type'] = test['Outlet_Location_Type'].str[-1].astype(int)

# Label Encoding for Ordinal Data
encoder = LabelEncoder()
ordinal_features = ['Item_Fat_Content', 'Outlet_Type', 'Outlet_Location_Type']
for feature in ordinal_features:
    train[feature] = encoder.fit_transform(train[feature])
    test[feature] = encoder.transform(test[feature])

# One Hot Encoding for 'Item_Type' variable
train = pd.get_dummies(train, columns=['Item_Type', 'Item_Identifier', 'Outlet_Identifier'], drop_first=True)
test = pd.get_dummies(test, columns=['Item_Type', 'Item_Identifier', 'Outlet_Identifier'], drop_first=True)

# Aligning columns of test data with train data
missing_cols = set(train.columns) - set(test.columns)
for col in missing_cols:
    test[col] = 0
test = test[train.columns]

# Dropping additional columns
identifier_columns = [col for col in train.columns if 'Item_Identifier' in col]
train.drop(labels=identifier_columns, axis=1, inplace=True)
test.drop(labels=identifier_columns, axis=1, inplace=True)

# Preparing data for modeling
y = train['Item_Outlet_Sales']
X = train.drop('Item_Outlet_Sales', axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Linear Regression model
lin_reg_model = LinearRegression()

# Fit the Linear Regression model
lin_reg_model.fit(X_train, y_train)

# Predictions for Linear Regression on the test data
lin_reg_predictions = lin_reg_model.predict(X_test)

# Evaluation metrics for Linear Regression
lin_reg_mse = mean_squared_error(y_test, lin_reg_predictions)
lin_reg_rmse = math.sqrt(lin_reg_mse)
lin_reg_r2 = r2_score(y_test, lin_reg_predictions)

lin_reg_results = {
    'Training Score': lin_reg_model.score(X_train, y_train),
    'Test Score': lin_reg_model.score(X_test, y_test),
    'RMSE': lin_reg_rmse,
    'R2 Score': lin_reg_r2
}

# Proceeding with Lasso Regression
steps = [
    ('scaler', StandardScaler()),
    ('poly', PolynomialFeatures(degree=2)),
    ('model', Lasso(alpha=0.2, fit_intercept=True))
]
lasso_pipeline = Pipeline(steps)
lasso_pipeline.fit(X_train, y_train)

# Predictions and evaluation for Lasso Regression
lasso_predictions = lasso_pipeline.predict(X_test)
lasso_mse = mean_squared_error(y_test, lasso_predictions)
lasso_rmse = math.sqrt(lasso_mse)
lasso_r2 = r2_score(y_test, lasso_predictions)

lasso_results = {
    'Training Score': lasso_pipeline.score(X_train, y_train),
    'Test Score': lasso_pipeline.score(X_test, y_test),
    'RMSE': lasso_rmse,
    'R2 Score': lasso_r2
}

lin_reg_results, lasso_results

# Checking if 'Item_Outlet_Sales' column exists in the test dataset
if 'Item_Outlet_Sales' in test.columns:
    test = test.drop('Item_Outlet_Sales', axis=1)
else:
    test = test
# Final predictions on test data using Lasso
final_test_preds = lasso_pipeline.predict(test)
# 20) Saving The Final Model
# Saving model to pickle file
with open("BigMart_Sales_Model.pkl", "wb") as file: # file is a variable for storing the newly created file.
    pickle.dump(lasso_pipeline, file)