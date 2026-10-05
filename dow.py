def isLeapYear(year):
    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    if year % 4 == 0:
        return True

    return False

def getDayOfTheWeek(year, month, day):
    month_codes = [1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]

    days_of_week = [
        "Saturday",
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday"
    ]

    last_two_digits = year % 100

    number_of_twelves = last_two_digits // 12

    remainder = last_two_digits % 12

    number_of_fours = remainder // 4

    month_code = month_codes[month - 1]

    if isLeapYear(year) and (month == 1 or month == 2):
        month_code -= 1

    century_codes = {
        16: 6,
        17: 4,
        18: 2,
        19: 0,
        20: 6,
        21: 4
    }

    century = year // 100

    month_code += century_codes[century]

    total = (
        number_of_twelves
        + remainder
        + number_of_fours
        + day
        + month_code
    )

    day_number = total % 7

    return days_of_week[day_number]

def makeCalendar():
    year = 2026

    days_in_month = [
        31, 28, 31, 30, 31, 30,
        31, 31, 30, 31, 30, 31
    ]

    if isLeapYear(year):
        days_in_month[1] = 29

    for month in range(1, 13):
        for day in range(1, days_in_month[month - 1] + 1):
            day_of_week = getDayOfTheWeek(year, month, day)
            print(f"{month}-{day}-{year} is a {day_of_week.lower()}.")