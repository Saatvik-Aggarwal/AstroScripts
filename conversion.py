# enter what type of conversion you want

# distance, wavelength, luminosity, radius, mass, temperature 

conversionType = input("Enter 'd' for distance, 'w' for wavelength, 'l' for luminosity, 'r' for radius, 'm' for mass, or 't' for temperature")

if (conversionType == 'd'):
    inputUnits = input("Enter 'pc' for parsecs, 'ly' for light years, 'au' for astronomical units, or 'm' for meters: ")
    distance = float(input("Enter distance in " + inputUnits + ": "))
    if (inputUnits == 'pc'):
        # print conversions to all other units
        print("Conversions to other units:")
        print("Light years: ", distance * 3.26156)
        print("Astronomical units: ", distance * 206264.806)
        print("Meters: ", distance * 3.08567758e16)
    elif (inputUnits == 'ly'):
        # print conversions to all other units
        print("Conversions to other units:")
        print("Parsecs: ", distance / 3.26156)
        print("Astronomical units: ", distance * 63241.077)
        print("Meters: ", distance * 9.4607304725808e15)
    elif (inputUnits == 'au'):
        # print conversions to all other units
        print("Conversions to other units:")
        print("Parsecs: ", distance / 206264.806)
        print("Light years: ", distance / 63241.077)
        print("Meters: ", distance * 1.49597870691e11)
    elif (inputUnits == 'm'):
        # print conversions to all other units
        print("Conversions to other units:")
        print("Parsecs: ", distance / 3.08567758e16)
        print("Light years: ", distance / 9.4607304725808e15)
        print("Astronomical units: ", distance / 1.49597870691e11)

if (conversionType == 'w'):
    inputUnits = input("Enter 'nm' for nanometers, 'c' for colors")

    if (inputUnits == "nm"):
        # print corresponding colors 
        wavelength = float(input("Enter wavelength in nanometers: "))
        print("Corresponding colors:")
        if (wavelength >= 380 and wavelength <= 450):
            print("Violet")
        elif (wavelength >= 450 and wavelength <= 485):
            print("Blue")
        elif (wavelength >= 485 and wavelength <= 500):
            print("Cyan")
        elif (wavelength >= 500 and wavelength <= 565):
            print("Green")
        elif (wavelength >= 565 and wavelength <= 590):
            print("Yellow")
        elif (wavelength >= 590 and wavelength <= 625):
            print("Orange")
        elif (wavelength >= 625 and wavelength <= 750):
            print("Red")
    elif (inputUnits == "c"):
        # print all colors and their corresponding wavelengths
        print("Violet - 380 nm to 450 nm")
        print("Blue - 450 nm to 485 nm")
        print("Cyan - 485 nm to 500 nm")
        print("Green - 500 nm to 565 nm")
        print("Yellow - 565 nm to 590 nm")
        print("Orange - 590 nm to 625 nm")
        print("Red - 625 nm to 750 nm")

if (conversionType == 'l'):
    inputUnits = input("Enter 'W' for watts or 'L' for solar luminosities:")
    if (inputUnits == "W"):
        # convert W to solar luminosities
        luminosity = float(input("Enter luminosity in watts: "))
        print("Solar luminosities:")
        print(luminosity / 3.828e26)
    elif (inputUnits == "L"):
        # convert solar luminosities to W
        luminosity = float(input("Enter luminosity in solar luminosities: "))
        print("Watts:")
        print(luminosity * 3.828e26)

if (conversionType == 'r'):
    inputUnits = input("Enter 'm' for meters or 'r' for solar radii:")
    if (inputUnits == "m"):
        # convert meters to solar radii
        radius = float(input("Enter radius in meters: "))
        print("Solar radii:")
        print(radius / 6.957e8)
    elif (inputUnits == "r"):
        # convert solar radii to meters
        radius = float(input("Enter radius in solar radii: "))
        print("Meters:")
        print(radius * 6.957e8)

if (conversionType == 'm'):
    inputUnits = input("Enter 'kg' for kilograms or 'm' for solar masses:")
    if (inputUnits == "kg"):
        # convert kilograms to solar masses
        mass = float(input("Enter mass in kilograms: "))
        print("Solar masses:")
        print(mass / 1.989e30)
    elif (inputUnits == "m"):
        # convert solar masses to kilograms
        mass = float(input("Enter mass in solar masses: "))
        print("Kilograms:")
        print(mass * 1.989e30)

if (conversionType == 't'):
    inputUnits = input("Enter 'K' for Kelvin and 'T' for solar temperatures")
    if (inputUnits == "K"):
        # convert Kelvin to solar temperatures
        temperature = float(input("Enter temperature in Kelvin: "))
        print("Solar temperatures:")
        print(temperature / 5778)
    elif (inputUnits == "T"):
        # convert solar temperatures to Kelvin
        temperature = float(input("Enter temperature in solar temperatures: "))
        print("Kelvin:")
        print(temperature * 5778)
    

        

