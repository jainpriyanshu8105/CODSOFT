# ==========================================
#        CODSOFT - PYTHON CALCULATOR
#        Developed by: Priyanshu
# ==========================================

def show_menu():
    print("\n" + "=" * 40)
    print("        PYTHON CALCULATOR")
    print("=" * 40)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (^)")
    print("7. Floor Division (//)")
    print("8. Exit")
    print("=" * 40)


def get_numbers():
    while True:
        try:
            num1 = float(input("Enter First Number : "))
            num2 = float(input("Enter Second Number : "))
            return num1, num2
        except ValueError:
            print("\n❌ Invalid Input! Please enter numbers only.\n")


while True:
    show_menu()

    choice = input("Choose an Option (1-8): ")

    if choice == "8":
        print("\nThank you for using Python Calculator ❤️")
        print("Have a Great Day!")
        break

    if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("\n❌ Invalid Choice! Please select between 1 to 8.")
        continue

    num1, num2 = get_numbers()

    if choice == "1":
        result = num1 + num2
        operation = "+"

    elif choice == "2":
        result = num1 - num2
        operation = "-"

    elif choice == "3":
        result = num1 * num2
        operation = "*"

    elif choice == "4":
        if num2 == 0:
            print("\n❌ Error! Division by zero is not allowed.")
            continue
        result = num1 / num2
        operation = "/"

    elif choice == "5":
        if num2 == 0:
            print("\n❌ Error! Modulus by zero is not allowed.")
            continue
        result = num1 % num2
        operation = "%"

    elif choice == "6":
        result = num1 ** num2
        operation = "^"

    elif choice == "7":
        if num2 == 0:
            print("\n❌ Error! Floor Division by zero is not allowed.")
            continue
        result = num1 // num2
        operation = "//"

    print("\n" + "-" * 40)
    print(f"Result : {num1} {operation} {num2} = {result}")
    print("-" * 40)

    again = input("\nDo you want another calculation? (Y/N): ").strip().lower()

    if again != "y":
        print("\nThank you for using Python Calculator ❤️")
        break