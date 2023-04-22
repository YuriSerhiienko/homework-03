from datetime import datetime, timedelta
birthdays_per_week = {
    'Monday': [],
    'Tuesday': [],
    'Wednesday': [],
    'Thursday': [],
    'Friday': [],
    'Saturday': [],
    'Sunday': []
}

today = datetime.now().date()
current_year = today.year
week_start = today + timedelta(days=7)
week_end = today + timedelta(days=13)
day_of_week = today.weekday()

idx = (week_start.weekday() + 1) % 7
sat = week_start - timedelta(7+idx-6)
sun = week_start - timedelta(7+idx-7)

def get_birthdays_per_week(users):
    for employee in users:
        birthday = datetime.strptime(employee["birthday"], "%Y-%m-%d").date().replace(year=current_year)
        if week_start <= birthday <= week_end:
            birthday_weekday = birthday.strftime('%A')
            birthdays_per_week[birthday_weekday].append(employee["name"])
        if sat <= birthday <= sun:
            birthdays_per_week['Monday'].append(employee["name"])
                 
    for weekday, names in birthdays_per_week.items():
        if names:
            print(f"{weekday}: {', '.join(names)}")

