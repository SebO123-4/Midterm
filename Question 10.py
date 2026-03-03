def days_since_birthday(birthday):
    """
    Calculate how many days have passed since a birthday,
    counting only full years (not birth year and not current year).

    :param birthday: date in format "DD-MM-YYYY"
    :return: number of days in full years between
    """

    parts = birthday.split("-")
    birth_year = int(parts[2])

    current_year = 2026  # set manually

    total_days = 0

    # Loop through full years only
    for year in range(birth_year + 1, current_year):

        # Check for leap year
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            total_days += 366
        else:
            total_days += 365

    return total_days

user_birthday = input("Enter your birthday (DD-MM-YYYY): ")
result = days_since_birthday(user_birthday)
print("Days in full years since your birth:", result)

#first i define my function
#then fix the problem of loop years by adding 366 instead of 365
#finally, the function returns the total days
#I also added an input feature so that people can type in their birthdays