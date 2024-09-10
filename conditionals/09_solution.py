

leapYear = 2000

if (leapYear % 400 == 0) or (leapYear % 4 == 0 and leapYear % 100 != 0):
    print(leapYear, "is a leap year")
else:
    print(leapYear, "is not a leap year")


