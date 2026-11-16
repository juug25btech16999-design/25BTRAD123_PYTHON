Title : Unit Converter

Code :

print("===== UNIT CONVERTER =====")

print("1. Centimeters to Meters")
print("2. Meters to Kilometers")
print("3. Kilograms to Grams")
print("4. Celsius to Fahrenheit")

choice = int(input("Enter your choice (1-4): "))
if choice == 1:
cm = float(input("Enter length in centimeters: "))
m = cm / 100
print("Length in meters =", m)
elif choice == 2:
m = float(input("Enter length in meters: "))
km = m / 1000
print("Length in kilometers =", km)
elif choice == 3:
kg = float(input("Enter weight in kilograms: "))
g = kg * 1000
print("Weight in grams =", g)
elif choice == 4:
c = float(input("Enter temperature in Celsius: "))

f = (c * 9/5) + 32
print("Temperature in Fahrenheit =", f)

else:
print("Invalid Choice!”)
