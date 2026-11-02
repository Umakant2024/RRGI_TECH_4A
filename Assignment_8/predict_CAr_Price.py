
import pandas as pd
import joblib

# Load the saved machine learning model
model = joblib.load("car_price_model.pkl")

print("=" * 40)
print("       CAR PRICE PREDICTION")
print("=" * 40)

# Get car details from the user
brand = input("Enter car brand (e.g., Hyundai): ").strip()
car_model = input("Enter car model (e.g., i20): ").strip()

year = int(input("Enter manufacturing year: "))
km_driven = int(input("Enter kilometres driven: "))

fuel = input("Enter fuel type (Petrol/Diesel/CNG/Electric): ").strip()
transmission = input("Enter transmission (Manual/Automatic): ").strip()

owner_count = int(input("Enter owner count (1, 2, 3, etc.): "))
seller_type = input("Enter seller type (Individual/Dealer/Trustmark Dealer): ").strip()

# Arrange the inputs in the same format as the training data
car_data = pd.DataFrame([{
    "brand": brand,
    "model": car_model,
    "year": year,
    "km_driven": km_driven,
    "fuel": fuel,
    "transmission": transmission,
    "owner_count": owner_count,
    "seller_type": seller_type
}])

# Predict the selling price
predicted_price = model.predict(car_data)[0]

# Display the result
print("\n" + "=" * 40)
print(f"Predicted Selling Price: ₹{predicted_price:.2f} lakh")
print(f"Approximate Price: ₹{predicted_price * 100000:,.0f}")
print("=" * 40)

print("\nNote: This is an estimated price, not a guaranteed market value.")
