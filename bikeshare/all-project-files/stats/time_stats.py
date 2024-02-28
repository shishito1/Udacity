import time

def get_time_stats(df):
    """Display statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Get the most common month and day of the week.
    print('Most common month: ', df['month'].mode()[0])
    print('Most common day of the week: ', df['day_of_week'].mode()[0])

    # Get the most common start hour.
    start_hour = df['Start Time'].dt.hour
    print('Most common start hour: ', start_hour.mode()[0])

    duration = time.time() - start_time
    print("\n\nThis took {} seconds.".format(duration))
    print('-'*40)
    