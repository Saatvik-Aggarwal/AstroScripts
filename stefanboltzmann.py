import numpy as np
# stefan-boltzmann constant
sigma = 5.670373e-8
# formula 
# L = sigma * epsilon * A * T^4
# ask user if they want to calculate temperature or area

choice = input("Enter 'T' to calculate temperature, 'A' to calculate area, 'epsilon' to calculate emissivity, or 'L' to calculate luminosity: ")


if (choice == "T"):
    # calculate temperature
    A = float(input("Enter area in m^2: "))
    L = float(input("Enter luminosity in W: "))
    epsilon = float(input("Enter emissivity (1 if unknown): "))
    
    T = (L / (sigma * epsilon * A))**(1/4)
    print("Temperature is (kelvin): ", T)

if (choice == "A"):
    # calculate area
    T = float(input("Enter temperature in kelvin: "))
    L = float(input("Enter luminosity in W: "))
    epsilon = float(input("Enter emissivity (1 if unknown): "))
    
    A = (L / (sigma * epsilon * T**4))
    print("Area is (m^2): ", A)
    # print radius as well
    R = (A / (4 * np.pi))**(1/2)
    print("Radius is (m): ", R)

if (choice == "epsilon"):
    # calculate emissivity
    T = float(input("Enter temperature in kelvin: "))
    L = float(input("Enter luminosity in W: "))
    A = float(input("Enter area in m^2: "))
    
    epsilon = L / (sigma * A * T**4)
    print("Emissivity is: ", epsilon)

if (choice == "L"):
    # calculate luminosity
    T = float(input("Enter temperature in kelvin: "))
    A = float(input("Enter area in m^2: "))
    epsilon = float(input("Enter emissivity (1 if unknown): "))
    
    L = sigma * epsilon * A * T**4
    print("Luminosity is (W): ", L)
