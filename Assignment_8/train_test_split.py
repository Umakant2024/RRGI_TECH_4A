
import pandas as pd
from sklearn.model_selection import train_test_split

# Load the cleaned dataset
df = pd.read_csv("cleaned_car_data.csv")

# Separate input features (X) and target (y)
X = df.drop("selling_price_lakh", axis=1)
y = df["selling_price_lakh"]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Display the results
print("Original dataset shape:", df.shape)
print("Training features shape:", X_train.shape)
print("Testing features shape:", X_test.shape)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))

print("\nDataset split completed successfully!")
