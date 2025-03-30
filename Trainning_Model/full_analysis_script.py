import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score, RandomizedSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
import joblib

# Step 1: Generate Synthetic Dataset
def generate_dataset(filename='dataset.csv', num_samples=1000):
    np.random.seed(42)
    
    data = {
        'feature1': np.random.normal(loc=50, scale=10, size=num_samples),
        'feature2': np.random.uniform(low=0, high=100, size=num_samples),
        'feature3': np.random.binomial(n=1, p=0.5, size=num_samples),
        'feature4': np.random.poisson(lam=5, size=num_samples),
        'category': np.random.choice(['A', 'B', 'C'], size=num_samples),
        'target': np.random.normal(loc=0, scale=1, size=num_samples)
    }
    
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"{filename} has been created.")

# Step 2: Load and Explore Dataset
def explore_data(filename='dataset.csv'):
    df = pd.read_csv(filename)
    
    print("Columns in the DataFrame:", df.columns.tolist())
    
    print("Descriptive Statistics:")
    print(df.describe(include='all'))
    
    print("Missing Values:")
    print(df.isnull().sum())
    
    # Plot distributions
    plt.figure(figsize=(14, 6))
    
    plt.subplot(1, 2, 1)
    sns.histplot(df['target'], kde=True)
    plt.title('Distribution of Target Variable')

    plt.subplot(1, 2, 2)
    sns.histplot(df['feature1'], kde=True)
    plt.title('Distribution of Feature1')
    
    plt.tight_layout()
    plt.show()
    
    return df

# Step 3: Data Preprocessing
def preprocess_data(df):
    X = df.drop('target', axis=1)
    y = df['target']
    
    categorical_features = ['category']
    numerical_features = X.select_dtypes(include=['float64', 'int64']).columns.tolist()
    
    missing_categorical = [col for col in categorical_features if col not in X.columns]
    if missing_categorical:
        raise ValueError(f"Categorical features not found in DataFrame: {missing_categorical}")
    
    missing_numerical = [col for col in numerical_features if col not in X.columns]
    if missing_numerical:
        raise ValueError(f"Numerical features not found in DataFrame: {missing_numerical}")
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numerical_features),
            ('cat', OneHotEncoder(drop='first', sparse_output=False), categorical_features)
        ]
    )
    
    X_processed = preprocessor.fit_transform(X)
    
    print(f"Processed data shape: {X_processed.shape}")
    
    X_train, X_test, y_train, y_test = train_test_split(X_processed, y, test_size=0.2, random_state=42)
    
    feature_names = (
        numerical_features + 
        preprocessor.transformers_[1][1].get_feature_names_out(categorical_features).tolist()
    )
    
    return X_train, X_test, y_train, y_test, preprocessor, feature_names

# Step 4: Model Training and Evaluation
def evaluate_models(X_train, X_test, y_train, y_test):
    models = {
        'Linear Regression': LinearRegression(),
        'Decision Tree': DecisionTreeRegressor(),
        'Random Forest': RandomForestRegressor(),
        'SVM': SVR()
    }
    
    plt.figure(figsize=(12, 8))
    
    for i, (name, model) in enumerate(models.items(), 1):
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        
        print(f"\n{name} Performance:")
        print(f"R² Score: {r2_score(y_test, y_pred)}")
        print(f"RMSE: {mean_squared_error(y_test, y_pred, squared=False)}")
        print(f"MAE: {mean_absolute_error(y_test, y_pred)}")
        
        cv_scores = cross_val_score(model, X_train, y_train, cv=5, scoring='r2')
        print(f"Mean CV R² Score: {cv_scores.mean()}")
        
        # Plot predictions vs actual values
        plt.subplot(2, 2, i)
        plt.scatter(y_test, y_pred, alpha=0.5)
        plt.xlabel('Actual Values')
        plt.ylabel('Predicted Values')
        plt.title(f'{name} Predictions')
    
    plt.tight_layout()
    plt.show()

# Step 5: Hyperparameter Tuning
def tune_hyperparameters(X_train, y_train):
    param_distributions = {
        'n_estimators': [100, 200, 300],
        'max_depth': [None, 10, 20, 30]
    }
    
    random_search = RandomizedSearchCV(RandomForestRegressor(), param_distributions, n_iter=10, cv=5, random_state=42)
    random_search.fit(X_train, y_train)
    best_model = random_search.best_estimator_
    
    print("\nBest Parameters from Random Search:")
    print(random_search.best_params_)
    
    return best_model

# Step 6: Model Testing
def test_best_model(best_model, X_test, y_test, feature_names):
    y_pred_best = best_model.predict(X_test)
    print("\nBest Model Performance:")
    print(f"R² Score: {r2_score(y_test, y_pred_best)}")
    print(f"RMSE: {mean_squared_error(y_test, y_pred_best, squared=False)}")
    print(f"MAE: {mean_absolute_error(y_test, y_pred_best)}")

    # Plot feature importance if Random Forest is used
    if isinstance(best_model, RandomForestRegressor):
        feature_importances = best_model.feature_importances_
        plt.figure(figsize=(10, 6))
        sorted_idx = np.argsort(feature_importances)
        plt.barh(range(len(sorted_idx)), feature_importances[sorted_idx], align='center')
        plt.yticks(range(len(sorted_idx)), np.array(feature_names)[sorted_idx])
        plt.xlabel('Feature Importance')
        plt.title('Feature Importances from Random Forest')
        plt.show()

# Step 7: Model Deployment
def deploy_model(best_model):
    joblib.dump(best_model, 'best_model.joblib')
    print("Best model saved to best_model.joblib")

# Main function to execute the workflow
def main():
    generate_dataset()
    df = explore_data()
    X_train, X_test, y_train, y_test, preprocessor, feature_names = preprocess_data(df)
    evaluate_models(X_train, X_test, y_train, y_test)
    best_model = tune_hyperparameters(X_train, y_train)
    test_best_model(best_model, X_test, y_test, feature_names)
    deploy_model(best_model)

if __name__ == "__main__":
    main()
