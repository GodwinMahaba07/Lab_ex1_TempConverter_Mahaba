
temperature = float(input("Enter a temperature: "))
print("Select the conversion type:")
print("1. From Celsius to Fahrenheit")
print("2. From Fahrenheit to Celsius")
conversion_type = int(input("Enter your choice (1 or 2): "))


if conversion_type == 1:
    result = (temperature * 9/5) + 32
    print(f"{temperature}°C is equal to {result}°F")
elif conversion_type == 2:
    result = (temperature - 32) * 5/9
    print(f"{temperature}°F is equal to {result}°C")
else:
    print("Invalid conversion type. Please try again.")