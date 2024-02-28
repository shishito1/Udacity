def filter_by_month(df, month, months):
    """Filter by month from January to June."""
    if month != 'all':
        month = months.index(month) + 1
        df = df[df['month'] == month]

def filter_by_day(df, day):
    """Filter by day of the week: Monday, Tuesday, etc."""
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    