import numpy as np
# calculate distance modulus 

# prompt what to solve for from user (apparent magnitude or distance or absolute magnitude)

x = input("Enter 'm' to solve for apparent magnitude, 'M' to solve for absolute magnitude, or 'd' to solve for distance: ")

if (x == 'm'):
    M = float(input("Enter absolute magnitude: "))
    d = float(input("Enter distance in parsecs: "))
    m = M - 5 * (np.log10(d) - 1)
    print("Apparent magnitude is: ", m)

if (x == 'M'):
    m = float(input("Enter apparent magnitude: "))
    d = float(input("Enter distance in parsecs: "))
    M = m + 5 * (np.log10(d) - 1)
    print("Absolute magnitude is: ", M)

if (x == 'd'):
    M = float(input("Enter absolute magnitude: "))
    m = float(input("Enter apparent magnitude: "))
    d = 10**((M - m) / 5)
    print("Distance is: ", d)