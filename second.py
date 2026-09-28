import pandas as pd

# Stable raw dataset link
url = "https://raw.githubusercontent.com/selva86/datasets/master/Churn_Modelling.csv"
df = pd.read_csv(url)

# Display the first 5 rows to verify it loaded correctly
print(df)

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# 1. Load the Dataset
url = "https://raw.githubusercontent.com/selva86/datasets/master/Churn_Modelling.csv"
df = pd.read_csv(url)
print("Dataset loaded successfully! Shape:", df.shape)

# 2. Preprocess Data
# Drop useless identifier columns
df = df.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1)

# Convert text/categorical columns ('Geography', 'Gender') into numbers
df = pd.get_dummies(df, columns=['Geography', 'Gender'], drop_first=True)

# Separate Independent features (X) and Dependent target variable (y -> Exited)
X = df.drop('Exited', axis=1).values
y = df['Exited'].values

# Split data: 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature Scaling (Crucial for Neural Networks so values range uniformly)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 3. Build the Artificial Neural Network (ANN) Architecture
model = Sequential([
    Dense(16, activation='relu', input_shape=(X_train.shape[1],)), # Hidden Layer 1
    Dense(8, activation='relu'),                                 # Hidden Layer 2
    Dense(1, activation='sigmoid')                               # Output Layer (0 or 1 probability)
])

# 4. Compile the Model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

print("\nTraining the ANN Model...")
# 5. Train the Model
history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.1, verbose=1)

# 6. Evaluate on Test Data
print("\nEvaluating Model on Test Data:")
y_pred_prob = model.predict(X_test)
y_pred = (y_pred_prob > 0.5).astype(int)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))