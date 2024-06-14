import calendar


def getMonthCalender(year, month):
    cal = calendar.TextCalendar()
    print(cal.formatmonth(year, month))


getMonthCalender(2024, 6)