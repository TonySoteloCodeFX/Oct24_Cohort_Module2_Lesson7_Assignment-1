def fahrenheit_to_celsius():
    celsius = round((fahrenheit - 32) * 5/9)
    print(f"{fahrenheit} degrees Fahrenheit")
    print("Is the same as")
    print(f"{celsius} degrees Celsius")

try:
    print("-" * 50)
    print("Welcome to the Weather Forecast Application")
    fahrenheit = int(input("Enter the Fahrenheit temperature: "))
    print("-" * 50)
    if fahrenheit.is_integer:
        fahrenheit_to_celsius()
except ValueError:
    print("-" * 50)
    print("You can only use numbers. Please try again.")
finally:
    print("-" * 50)
    print("Thank you for using the Weather Forecast Application.")
    print("-" * 50)