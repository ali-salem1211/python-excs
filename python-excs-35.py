from datetime import datetime, date

# Today's date
today = date.today()
print("Today's date:", today)

# What day of the week it is
print("Day of the week:", today.strftime("%A"))

# Days until New Year
new_year = date(today.year + 1, 1, 1)
days_until_ny = (new_year - today).days
print("Days until New Year:", days_until_ny)
