import dow


def getDayOfTheWeekForUserDate():
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))
    day = int(input("Enter day: "))

    day_of_week = dow.getDayOfTheWeek(year, month, day)

    print(f"The day of the week is {day_of_week}.")


dow.makeCalendar()

getDayOfTheWeekForUserDate()