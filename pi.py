"""
Daniel Jian
Module 08 Lab Assignment
Part B

This program returns the value of pi at request.
"""

from math import pi

preference = input("Do you want an approximation of pi? (Y/N) ").lower()

if preference == "y":
    print("Pi equals 3.14")
else:
    print("Pi equals " + pi)
