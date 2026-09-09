import csv
from datetime import datetime



# 1. CALCULATE ELECTRICITY BILL


def calculate_bill(units):

    if units <= 100:
        energy_charge = units * 5
    elif units <= 200:
        energy_charge = (100 * 5) + ((units - 100) * 7)
    elif units <= 300:
        energy_charge = ( (100 * 5)    + (100 * 7)     + ((units - 200) * 10)  )
    else:
        energy_charge = ((100 * 5) + (100 * 7)+ (100 * 10) + ((units - 300) * 12))

    fixed_charge = 100

    subtotal = energy_charge + fixed_charge

    tax = subtotal * 5 / 100

    total_bill = subtotal + tax

    return energy_charge, fixed_charge, tax, total_bill
# 2. SAVE BILL
def save_bill(bill_number, date_time,name,customer_id,units,energy_charge,   fixed_charge,tax, total_bill):
    with open("bills.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([ bill_number,date_time,name,  customer_id,units,energy_charge, fixed_charge,tax, total_bill])

# 3. VIEW ALL BILLS

def view_bills():
    try:
        with open("bills.csv", "r") as file:
            reader = csv.reader(file)
            print("\n")
            print("=" * 100)
            print("                ALL BILL HISTORY")
            print("=" * 100)

            found = False

            for row in reader:

                found = True

                print(
                    f"Bill No: {row[0]} | "
                    f"Date: {row[1]} | "
                    f"Name: {row[2]} | "
                    f"ID: {row[3]} | "
                    f"Units: {row[4]} | "
                    f"Total: ₹{row[8]}"
                )

            if not found:
                print("No bills available.")

            print("=" * 100)
    except FileNotFoundError:

        print("\nNo bill history found.")

# 4. SEARCH CUSTOMER
def search_customer(customer_id):
    try:
        with open("bills.csv", "r") as file:
            reader = csv.reader(file)
            found = False
            for row in reader:
                if row[3] == customer_id:
                    found = True
                    print("\n")
                    print("=" * 50)
                    print("             CUSTOMER BILL")
                    print("=" * 50)
                    print("Bill Number   :", row[0])
                    print("Date & Time   :", row[1])
                    print("Customer Name :", row[2])
                    print("Customer ID   :", row[3])
                    print("Units         :", row[4])
                    print("-" * 50)
                    print("Energy Charge :", "₹", row[5])
                    print("Fixed Charge  :", "₹", row[6])
                    print("Tax           :", "₹", row[7])
                    print("-" * 50)
                    print("TOTAL BILL    :", "₹", row[8])
                    print("=" * 50)
            if not found:
                print("\nCustomer not found!")

    except FileNotFoundError:

        print("\nNo bill history found.")

# 5. DELETE CUSTOMER BILL
def delete_customer(customer_id):
    try:
        with open("bills.csv", "r") as file:
            rows = list(csv.reader(file))
        new_rows = []
        deleted = False
        for row in rows:
            if row[3] == customer_id:
                deleted = True
            else:
                new_rows.append(row)
        if deleted:
            with open("bills.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(new_rows)
            print("\nBill deleted successfully!")
        else:
            print("\nCustomer not found!")
    except FileNotFoundError:
        print("\nNo bill history found.")

# 6. GENERATE NEW BILL

def generate_bill():
    print("\n")
    print("=" * 50)
    print("              GENERATE NEW BILL")
    print("=" * 50)

    name = input("Enter Customer Name: ")
    customer_id = input("Enter Customer ID: ")
    try:
        units = float(input("Enter Units Consumed: "))
    except ValueError:
        print("Please enter a valid number!")

        return

    if units < 0:

        print("Units cannot be negative!")

        return

    # Calculate bill

    energy_charge, fixed_charge, tax, total_bill = calculate_bill(units)

    # Generate bill number

    bill_number = "EB" + datetime.now().strftime("%Y%m%d%H%M%S")

    # Current date and time

    date_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    # Display bill

    print("\n")
    print("=" * 50)
    print("              ELECTRICITY BILL")
    print("=" * 50)

    print("Bill Number   :", bill_number)
    print("Date & Time   :", date_time)

    print("-" * 50)

    print("Customer Name :", name)
    print("Customer ID   :", customer_id)
    print("Units Consumed:", units)

    print("-" * 50)

    print("Energy Charge :", "₹", energy_charge)
    print("Fixed Charge  :", "₹", fixed_charge)
    print("Tax (5%)      :", "₹", tax)

    print("-" * 50)

    print("TOTAL BILL    :", "₹", total_bill)

    print("=" * 50)

    # Save bill

    save_bill(
        bill_number,
        date_time,
        name,
        customer_id,
        units,
        energy_charge,
        fixed_charge,
        tax,
        total_bill
    )

    print("Bill saved successfully!")

# 7. MAIN MENU
while True:
    print("\n")
    print("=" * 50)
    print("           ELECTRICITY BILL SYSTEM")
    print("=" * 50)
    print("1. Generate New Bill")
    print("2. View All Bills")
    print("3. Search Customer")
    print("4. Delete Customer Bill")
    print("5. Exit")
    print("=" * 50)
    choice = input("Enter your choice: ")
    # Generate bill

    if choice == "1":

        generate_bill()


    # View bills

    elif choice == "2":

        view_bills()
    # Search customer
    elif choice == "3":
        customer_id = input("Enter Customer ID: ")
        search_customer(customer_id)
    # Delete bill
    elif choice == "4":
        customer_id = input("Enter Customer ID: ")
        delete_customer(customer_id)
    # Exit
    elif choice == "5":
        print("\nThank you for using Electricity Bill System!")
        break
    # Invalid choice
    else:
        print("\nInvalid choice! Please select 1-5.")