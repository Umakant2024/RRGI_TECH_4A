
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# 1. Load the cleaned dataset
df = pd.read_csv("cleaned_car_data.csv")

# 2. Separate features and target
X = df.drop("selling_price_lakh", axis=1)
y = df["selling_price_lakh"]

# 3. Identify categorical and numerical columns
categorical_columns = X.select_dtypes(
    include=["object"]
).columns.tolist()

numerical_columns = X.select_dtypes(
    exclude=["object"]
).columns.tolist()

print("Categorical columns:", categorical_columns)
print("Numerical columns:", numerical_columns)

# 4. Convert categorical text into numerical features
preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_columns
        ),
        ("numerical", "passthrough", numerical_columns)
    ]
)

# 5. Create the Random Forest model
model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        (
            "regressor",
            RandomForestRegressor(
                n_estimators=100,
                random_state=42
            )
        )
    ]
)

# 6. Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 7. Train the model
print("\nTraining the model...")
model.fit(X_train, y_train)

# 8. Make predictions
y_pred = model.predict(X_test)

# 9. Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel trained successfully!")
print(f"Mean Absolute Error (MAE): {mae:.2f} lakh")
print(f"R² Score: {r2:.3f}")

# 10. Compare actual and predicted prices
results = pd.DataFrame({
    "Actual Price (Lakh)": y_test.values,
    "Predicted Price (Lakh)": y_pred
})

print("\nSample Predictions:")
print(results.head(10))

# Save the trained model
joblib.dump(model, "car_price_model.pkl")

print("\nModel saved successfully as car_price_model.pkl")
