print("Ohm's Law Calculator")
print("1. Find Voltage (V)")
print("2. Find Current (I)")
print("3. Find Resistance (R)")

choice = int(input("Choose what you want to calculate (1/2/3): "))

if choice == 1:
    I = float(input("Enter current (A): "))
    R = float(input("Enter resistance (Ω): "))
    V = I * R
    print("Voltage =", V, "Volts")

elif choice == 2:
    V = float(input("Enter voltage (V): "))
    R = float(input("Enter resistance (Ω): "))
    I = V / R
    print("Current =", I, "Amperes")

elif choice == 3:
    V = float(input("Enter voltage (V): "))
    I = float(input("Enter current (A): "))
    R = V / I
    print("Resistance =", R, "Ohms")

else:
    print("Invalid choice")
