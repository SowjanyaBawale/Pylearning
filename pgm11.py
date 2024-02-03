#Leap year
year = int(input("Enter the year\n"))
is_leap_year = False

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    is_leap_year = True

print(f"{year} is {is_leap_year}")