print("Hello! This is a unit converter that converts kilometers into miles.")

while True:
    print("Enter a number of kilometers that you would like to convert into miles.")

    km: str = input("Kilometers: ")

    miles = float(km) * 0.621371192

    print("{0} kilometers is {1} miles.".format(km, miles))

    choice = input("Would you like to do another conversion (y/n): ")

    if choice.lower() != "y" and choice.lower() != "yes":
        break