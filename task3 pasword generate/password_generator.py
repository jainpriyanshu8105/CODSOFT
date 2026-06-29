# ==========================================
#     CODSOFT - PASSWORD GENERATOR
#     Developed by: Priyanshu
# ==========================================

import random
import string


print("=" * 45)
print("        PASSWORD GENERATOR")
print("=" * 45)

while True:
    try:
        length = int(input("Enter Password Length: "))

        if length <= 0:
            print("❌ Length must be greater than 0.\n")
            continue

        break

    except ValueError:
        print("❌ Please enter a valid number.\n")


characters = (
    string.ascii_letters +
    string.digits +
    string.punctuation
)

password = ""

for i in range(length):
    password += random.choice(characters)

print("\n" + "=" * 45)
print("Generated Password:")
print(password)
print("=" * 45)