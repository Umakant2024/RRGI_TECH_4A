
import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import joblib

# Load the trained model
try:
    model = joblib.load("car_price_model.pkl")
except FileNotFoundError:
    raise SystemExit(
        "Model not found! Run train_model.py first."
    )

# Create the main window
root = tk.Tk()
root.title("Car Price Prediction System")
root.geometry("700x650")
root.configure(bg="#eef3f8")
root.resizable(False, False)

# Heading
title = tk.Label(
    root,
    text="Car Price Prediction",
    font=("Arial", 22, "bold"),
    bg="#eef3f8",
    fg="#1c68c0"
)
title.pack(pady=20)

subtitle = tk.Label(
    root,
    text="Enter the car details below",
    font=("Arial", 11),
    bg="#eef3f8",
    fg="#555555"
)
subtitle.pack(pady=5)

# Form frame
form = tk.Frame(root, bg="white", padx=25, pady=20)
form.pack(padx=25, pady=15, fill="x")

# Input fields and dropdown choices
fields = [
    ("Brand", ["Maruti", "Hyundai", "Tata", "Honda", "Toyota",
               "Mahindra", "Kia", "Ford", "BMW", "Mercedes-Benz"]),
    ("Model", None),
    ("Year", None),
    ("Kilometres Driven", None),
    ("Fuel", ["Petrol", "Diesel", "CNG", "Electric"]),
    ("Transmission", ["Manual", "Automatic"]),
    ("Owner Count", ["1", "2", "3", "4", "5"]),
    ("Seller Type", ["Individual", "Dealer", "Trustmark Dealer"])
]

widgets = {}

for row, (label_text, options) in enumerate(fields):
    label = tk.Label(
        form,
        text=label_text,
        font=("Arial", 10, "bold"),
        bg="white",
        anchor="w"
    )
    label.grid(row=row, column=0, sticky="w", pady=7)

    if options:
        widget = ttk.Combobox(
            form,
            values=options,
            state="readonly",
            width=25
        )
        widget.current(0)
    else:
        widget = ttk.Entry(form, width=28)

    widget.grid(row=row, column=1, pady=7, padx=10)
    widgets[label_text] = widget


def predict_price():
    try:
        brand = widgets["Brand"].get().strip()
        car_model = widgets["Model"].get().strip()
        year = int(widgets["Year"].get())
        km_driven = int(widgets["Kilometres Driven"].get())
        fuel = widgets["Fuel"].get()
        transmission = widgets["Transmission"].get()
        owner_count = int(widgets["Owner Count"].get())
        seller_type = widgets["Seller Type"].get()

        if not brand or not car_model:
            messagebox.showerror(
                "Input Error",
                "Please enter the brand and model."
            )
            return

        if year < 1980 or year > 2026:
            messagebox.showerror(
                "Input Error",
                "Please enter a valid manufacturing year."
            )
            return

        if km_driven < 0 or owner_count < 1:
            messagebox.showerror(
                "Input Error",
                "Kilometres cannot be negative and owner count must be positive."
            )
            return

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

        predicted_price = model.predict(car_data)[0]

        result_label.config(
            text=(
                f"Estimated Price: ₹{predicted_price:.2f} lakh\n"
                f"Approximately ₹{predicted_price * 100000:,.0f}"
            ),
            fg="#087443"
        )

    except ValueError:
        messagebox.showerror(
            "Input Error",
            "Please enter valid numbers for year and kilometres driven."
        )
    except Exception as error:
        messagebox.showerror(
            "Prediction Error",
            f"Could not predict the price.\n{error}"
        )


# Predict button
predict_button = tk.Button(
    root,
    text="Predict Price",
    command=predict_price,
    font=("Arial", 12, "bold"),
    bg="#1769aa",
    fg="white",
    activebackground="#0d4778",
    activeforeground="white",
    relief="flat",
    padx=20,
    pady=10,
    cursor="hand2"
)
predict_button.pack(pady=10)

# Result area
result_label = tk.Label(
    root,
    text="Your predicted price will appear here",
    font=("Arial", 12, "bold"),
    bg="#eef3f8",
    fg="#333333",
    wraplength=480,
    justify="center"
)
result_label.pack(pady=15)

# Disclaimer
disclaimer = tk.Label(
    root,
    text="Note: Predictions use a synthetic demonstration dataset.",
    font=("Arial", 9),
    bg="#eef3f8",
    fg="#666666",
    wraplength=480
)
disclaimer.pack(pady=5)

root.mainloop()
