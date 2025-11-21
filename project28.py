import calendar
cal = calendar.TextCalendar()
for month in range(1, 13):
    print(calendar.month_name[month])
    print(cal.formatmonth(2025, month))