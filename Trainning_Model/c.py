# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score, RandomizedSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from scipy import stats

# 1. Data Exploration

# Load the dataset
df = pd.read_csv('Cost_of_Living_Index_by_Country_2024.csv')

# Display basic statistics and info
print(df.describe())
print(df.info())

# Print column names to identify possible features
print("Column names in dataset:", df.columns)

# Example: Create a synthetic target variable if needed
# Here we're just creating a random target for demonstration purposes
df['SyntheticTarget'] = np.random.rand(len(df))

# Visualize the distribution of numeric features
numeric_features = df.select_dtypes(include=['float64', 'int64']).columns
for feature in numeric_features:
    sns.histplot(df[feature])
    plt.title(f'Distribution of {feature}')
    plt.show()

# Visualize correlations
numeric_df = df.select_dtypes(include=['float64', 'int64'])  # Select only numeric columns
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# 2. Data Preprocessing

# Handle missing values
df.fillna(df.mean(numeric_only=True), inplace=True)  # Impute numerical features with mean

# Handle outliers (assuming Z-score method for numerical features)
z_scores = np.abs(stats.zscore(numeric_df))
df = df[(z_scores < 3).all(axis=1)]

# Encode categorical features (example: one-hot encoding)
df = pd.get_dummies(df)

# Print column names after encoding
print("Column names after encoding:", df.columns)

# Use the synthetic target column
target = 'SyntheticTarget'  # Use the synthetic target column

# Split the dataset into training and testing sets
X = df.drop(target, axis=1)
y = df[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Model Training and Evaluation

# Define models
models = {
    'Linear Regression': LinearRegression(),
    'Decision Tree': DecisionTreeRegressor(),
    'Random Forest': RandomForestRegressor(),
    'SVM': SVR()
}

# Train and evaluate models
for name, model in models.items():
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print(f"{name} - Train Score: {model.score(X_train, y_train)}")
    print(f"{name} - R²: {r2_score(y_test, predictions)}")
    print(f"{name} - RMSE: {mean_squared_error(y_test, predictions, squared=False)}")
    print(f"{name} - MAE: {mean_absolute_error(y_test, predictions)}")
    cv_scores = cross_val_score(model, X, y, cv=5)
    print(f"{name} - CV Scores: {cv_scores.mean()}\n")

# 4. Hyperparameter Tuning

# Define parameter distributions for RandomizedSearchCV
param_distributions = {
    'n_estimators': [10, 50, 100],
    'max_depth': [None, 10, 20],
}

# Initialize and fit RandomizedSearchCV
random_search = RandomizedSearchCV(RandomForestRegressor(), param_distributions, n_iter=10, cv=5, random_state=42)
random_search.fit(X_train, y_train)
print(f"Best Parameters: {random_search.best_params_}")

# 5. Model Testing and Analysis

# Test the best model
best_model = random_search.best_estimator_
test_predictions = best_model.predict(X_test)
print(f"Best Model R²: {r2_score(y_test, test_predictions)}")
print(f"Best Model RMSE: {mean_squared_error(y_test, test_predictions, squared=False)}")
print(f"Best Model MAE: {mean_absolute_error(y_test, test_predictions)}")

# Analyze performance and discuss limitations
print("Analysis:")
print("The best model achieved an R² of {:.2f}, RMSE of {:.2f}, and MAE of {:.2f}.".format(
    r2_score(y_test, test_predictions),
    mean_squared_error(y_test, test_predictions, squared=False),
    mean_absolute_error(y_test, test_predictions)
))
print("\nDiscuss limitations and potential improvements here.\n")

# 6. Unsupervised Learning Example: K-Means Clustering

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Perform K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X_scaled)

# Add cluster labels to DataFrame
df['Cluster'] = clusters

# Print column names for clustering
print("Column names for clustering:", df.columns)

# Replace 'Feature1' and 'Feature2' with actual feature names for plotting
# Ensure you use actual numeric columns in your DataFrame for visualization
# You may need to choose columns that are meaningful for clustering visualization

# Example with generic numeric features; replace with actual column names
if 'Feature1' in df.columns and 'Feature2' in df.columns:
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Feature1', y='Feature2', hue='Cluster', palette='viridis')
    plt.title('Clustering Results')
    plt.show()
else:
    print("Feature1 and Feature2 are not available. Choose appropriate columns for plotting.")
